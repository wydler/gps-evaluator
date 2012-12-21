library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

architecture evaluator_a of evaluator_e is
	signal sft_s	: std_logic;
	signal nxt_s	: std_logic_vector(7 downto 0);
	signal write_s	: std_logic;
	signal txrdy_s	: std_logic;
	signal trg_s	: std_logic;
	signal trg_rdy_s : std_logic;
	
	component uarttx_e is
		port(
			clk_i	: in std_logic;
			write_i	: in std_logic;
			rst_n_i	: in std_logic;
			data_i	: in std_logic_vector(7 downto 0);
			tx_o	: out std_logic;
			txrdy_o	: out std_logic
		);
	end component;
	
	component clkcntsrl_e is
		port(
			clka_i 		: in std_logic;
			clkb_i 		: in std_logic;
			gps_i 		: in std_logic;
			sft_i 		: in std_logic;
			rst_n_i 	: in std_logic;
			nxt_o		: out std_logic_vector(7 downto 0);
			trg_o 		: out std_logic
		);
	end component;
	
	component rising_edge_e is
		port(clk_i    : in std_logic;
			  rst_n_i  : in std_logic;
			  signal_i : in std_logic;
			  rising_o : out std_logic);
	end component;
begin
	clkcntsrl:clkcntsrl_e
	port map(
		clka_i	=> clka_i,
		clkb_i	=> clkb_i,
		gps_i 	=> gps_i,
		sft_i	=> sft_s,
		rst_n_i	=> rst_n_i,
		nxt_o	=> nxt_s,
		trg_o	=> trg_s
	);

	uarttx:uarttx_e
	port map(
		clk_i	=> clka_i,
		write_i	=> write_s,
		rst_n_i	=> rst_n_i,
		data_i	=> nxt_s,
		tx_o	=> tx_o,
		txrdy_o	=> txrdy_s
--		txrdy_o	=> sft_s
	);
	
	process( txrdy_s, trg_s, clka_i, rst_n_i )
	begin
		if rst_n_i = '0' then
			sft_s <= '1';
			write_s <= '0';
			trg_rdy_s <= '0';
		elsif clka_i'event and clka_i = '1' then
			if trg_s = '1' then
				trg_rdy_s <= '1';
			end if;
			
			if trg_rdy_s = '1' and txrdy_s = '1' then
				write_s <= '1';
				trg_rdy_s <= '0';
			elsif txrdy_s = '0' then
				write_s <= '0';
				sft_s <= '1';
			else
				sft_s <= '0';
			end if;
		end if;
	end process;

end evaluator_a;

