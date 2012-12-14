library ieee;
use ieee.std_logic_1164.all;

entity dualclkcnt_e is
	port(clka_i 	: in std_logic;
		 clkb_i 	: in std_logic;
		 gps_i 		: in std_logic;
		 rst_n_i 	: in std_logic;
		 cnta_o 	: out std_logic_vector(31 downto 0);
		 cntb_o 	: out std_logic_vector(31 downto 0);
		 syn_o 		: out std_logic
		 );
end dualclkcnt_e;
