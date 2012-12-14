library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity gpsclksrc_e is 
	port(
		clk_i		: in	std_logic;
		rst_n_i		: in	std_logic;
		gps_i		: in	std_logic;
		gpshalf_o	: out	std_logic;
		rising_o	: out	std_logic;
		falling_o	: out	std_logic
	);
end gpsclksrc_e;
