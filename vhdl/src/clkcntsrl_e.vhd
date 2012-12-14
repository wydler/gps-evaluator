library ieee;
use ieee.std_logic_1164.all;

entity clkcntsrl_e is
	port(	clka_i 		: in std_logic;
			clkb_i 		: in std_logic;
		 	gps_i 		: in std_logic;
		 	sft_i 		: in std_logic;
		 	rst_n_i 	: in std_logic;
			nxt_o		: out std_logic_vector(7 downto 0);
		 	trg_o 		: out std_logic
		 );
end clkcntsrl_e;
