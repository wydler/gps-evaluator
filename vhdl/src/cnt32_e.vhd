library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity cnt32_e is 
	port(
		clk_i	: in	std_logic;
		rst_i	: in	std_logic;
		cnt_o	: out	std_logic_vector(31 downto 0)
	);
end cnt32_e;
