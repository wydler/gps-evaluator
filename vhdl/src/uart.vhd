library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity uarttx_e is
	generic (txclkcount_g : positive := 1);	-- Number of bits for the count in the clock divider (default = 3 for clk/16)
	port(
		clk_i	: in std_logic;
		write_i	: in std_logic;
		rst_n_i	: in std_logic;
		data_i	: in std_logic_vector(7 downto 0);
		tx_o	: out std_logic;
		txrdy_o	: out std_logic);
end uarttx_e;


architecture uarttx_a of uarttx_e is
	constant paritymode_c : std_logic := '0';	-- initializing to 1 = odd parity, 0 = even parity
	signal write1_s, write2_s : std_logic;
	signal txdone1_s, txdone_s : std_logic;
	signal thr_s, tsr_s : std_logic_vector( 7 downto 0 );
	signal tag1_s, tag2_s : std_logic;
	signal txparity_s : std_logic;
	signal txclk_s : std_logic;
	signal paritycycle_s : std_logic;
	signal txdatardy_s : std_logic;
	signal cnt_s : std_logic_vector( txclkcount_g-1 downto 0 );
begin
   
-- Paritycycle = 1 on next to last cycle, this means when tsr[1] gets tag2.
paritycycle_s <= tsr_s(1) and
	not( tag2_s or tag1_s or tsr_s(7) or tsr_S(6) or
		tsr_s(5) or tsr_s(4) or tsr_s(3) or tsr_s(2) );

-- txdone = 1 when done shifting, this means when tx gets tag2.
txdone_s <= not( tag2_s or tag1_s or tsr_s(7) or tsr_s(6) or tsr_s(5) or
		tsr_s(4) or tsr_s(3) or tsr_s(2) or tsr_s(1) or tsr_s(0) );

-- Ready for new data to be written, when no data is in transmit hold register.
txrdy_o <= not txdatardy_s;

--Latch data[7:0] into the transmit hold register at posedge of write.
	thr_write : process( write_i, data_i, txdatardy_s )
	begin
		if write_i = '0' and txdatardy_s = '0' then
			thr_s <= data_i;
		end if;
	end process;

--// Toggle txclk every 2^txclkcount counts, which divides the clock by
--// 2*2^txclkcount, to generate the baud clock
	baud_clock_gen : process( clk_i, rst_n_i )
		variable count_indicator: std_logic_vector( txclkcount_g-1 downto 0 );
	begin
		count_indicator := ( others => '0' );
		if( rst_n_i ='0' ) then
			txclk_s <= '0';
			cnt_s <= (others => '0');
		elsif( clk_i='1' and clk_i'event ) then
			if( cnt_s = count_indicator) then
				txclk_s <= not txclk_s;
			end if;
			cnt_s <= cnt_s + 1;
		end if;
	end process;

	shift_out : process( txclk_s, rst_n_i )
	begin
		if( rst_n_i = '0' ) then
			tsr_s <= ( others => '0' );
			tag2_s <= '0';
			tag1_s <= '0';
			txparity_s <= paritymode_c;
			tx_o <= '1';
		--idle_reset
		elsif txclk_s = '1' and txclk_s'event then
			if (txdone_s='1' and txdatardy_s = '1') then
				--load_data
				tsr_s <= thr_s;
				tag2_s <= '1';
				tag1_s <= '1';
				txparity_s <= paritymode_c;
				tx_o <= '0';
			else
			--shift_data
			tsr_s <= '0'&tsr_s(7 downto 1);
			tsr_s(7) <= tag1_s;
			tag1_s <= tag2_s;
			tag2_s <= '0';
			txparity_s <= txparity_s xor tsr_s(0);
			if( txdone_s = '1' ) then
				tx_o <= '1';
				elsif( paritycycle_s = '1' ) then
					tx_o <= txparity_s;
				else
					tx_o <= tsr_s(0);
				end if;
			end if;
		end if;
	end process;

	process( clk_i, rst_n_i )
	begin
		if( rst_n_i='0' ) then
			txdatardy_s <= '0';
			write2_s <= '1';
			write1_s <= '1';
			txdone1_s <= '1';
			elsif clk_i = '1' and clk_i'event then
				if( write1_s = '1' and write2_s = '0' ) then
					txdatardy_s <= '1';
			elsif( txdone_s = '0' and txdone1_s = '1' ) then
				txdatardy_s <= '0';
		end if;
		write2_s <= write1_s;
		write1_s <= write_i;
		txdone1_s <= txdone_s;
		end if;
	end process;
end uarttx_a;
