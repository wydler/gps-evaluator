library ieee;
use ieee.std_logic_1164.all;

entity clkdiv_e is
	port(clk_i : in std_logic;
		 rst_i : in std_logic;
		 clk_o : out std_logic);
end clkdiv_e;