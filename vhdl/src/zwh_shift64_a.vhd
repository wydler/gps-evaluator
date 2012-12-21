library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;



architecture zwh_shift64_a of zwh_shift64_e is
	--signal buf_s	: unsigned(63 downto 0);
	signal syn_rising_s : std_logic;
	signal sft_rising_s : std_logic;
	
	component rising_edge_e is
		port(clk_i    : in std_logic;
			  rst_n_i  : in std_logic;
			  signal_i : in std_logic;
			  rising_o : out std_logic);
	end component;
begin
	syn_rising_edge: rising_edge_e
		port map(
			clk_i 		=> clk_i,
			rst_n_i 		=> rst_n_i,
			signal_i		=> syn_i,
			rising_o		=> syn_rising_s);
			
	sft_rising_edge: rising_edge_e
		port map(
			clk_i 		=> clk_i,
			rst_n_i 		=> rst_n_i,
			signal_i		=> sft_i,
			rising_o		=> sft_rising_s);
		
	process( clk_i, rst_n_i )
		variable buf_v : unsigned(63 downto 0);
	begin
		if rst_n_i = '0' then
			--buf_s <= (others=>'0');
			nxt_o <= (others=>'0');
			buf_v := (others=>'0');
		elsif clk_i'event and clk_i = '1' then
			if syn_rising_s = '1' then
				buf_v(63 downto 32) := unsigned(b_i);
				buf_v(31 downto 0) := unsigned(a_i);
				--buf_s <= buf_v;
			elsif sft_rising_s = '1' then
				buf_v := buf_v srl 8;
			end if;
			nxt_o <= std_logic_vector(buf_v(7 downto 0));
		end if;
	end process;
end zwh_shift64_a;