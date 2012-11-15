library ieee;
use ieee.std_logic_1164.all;

entity clkdiffpulse_e is
	port(a_i : in std_logic;
		 b_i : in std_logic;
		 rst_i : in std_logic;
		 p_o : out std_logic);
end clkdiffpulse_e;
