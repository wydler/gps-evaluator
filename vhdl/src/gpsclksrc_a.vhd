library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

architecture gpsclksrc_a of gpsclksrc_e is

	signal halfgps_s: std_logic;

	component tff
		port (	clk_i, rst_n_i 	: in std_logic;
				q_o				: out std_logic);
	end component;

	component rising_edge_e
		port (	clk_i, rst_n_i, signal_i 	: in std_logic;
				rising_o    				: out std_logic);
	end component;

	component falling_edge_e
		port (	clk_i, rst_n_i, signal_i 	: in std_logic;
				falling_o    				: out std_logic);
	end component;

begin
	gpstff:tff
	port map(
		clk_i => gps_i,
		rst_n_i => rst_n_i,
		q_o => halfgps_s);
		
	rising_edge:rising_edge_e
	port map(
		clk_i => clk_i,
		rst_n_i => rst_n_i,
		signal_i => halfgps_s,
		rising_o => rising_o);
	
	falling_edge:falling_edge_e
	port map(
		clk_i => clk_i,
		rst_n_i => rst_n_i,
		signal_i => halfgps_s,
		falling_o => falling_o);

	gpshalf_o <= halfgps_s;
end gpsclksrc_a;

