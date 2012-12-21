library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity evaluator_e is 
	port(
		clka_i		: in	std_logic;
		clkb_i		: in	std_logic;
		gps_i		: in	std_logic;
		rst_n_i		: in	std_logic;
		tx_o		: out 	std_logic;
		led_o			:out std_logic
	);
end evaluator_e;
