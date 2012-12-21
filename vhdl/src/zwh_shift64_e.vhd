library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity zwh_shift64_e is 
	port(
		clk_i		: in  std_logic;
		rst_n_i	: in	std_logic;
		sft_i		: in	std_logic;
		a_i		: in	std_logic_vector(31 downto 0);
		b_i		: in	std_logic_vector(31 downto 0);
		syn_i		: in	std_logic;
		nxt_o		: out	std_logic_vector(7 downto 0)
	);
end zwh_shift64_e;
