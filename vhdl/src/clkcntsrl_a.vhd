library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

architecture clkcntsrl_a of clkcntsrl_e is
	component dualclkcnt_e is
		port(	clka_i 	: in std_logic;
		 		clkb_i 	: in std_logic;
		 		gps_i 	: in std_logic;
		 		rst_n_i : in std_logic;
		 		cnta_o 	: out std_logic_vector(31 downto 0);
		 		cntb_o 	: out std_logic_vector(31 downto 0);
		 		syn_o 	: out std_logic);
	end component;

	component zwh_shift64_e is
		port(	clk_i	: in std_logic;
				rst_n_i	: in	std_logic;
				sft_i	: in	std_logic;
				a_i		: in	std_logic_vector(31 downto 0);
				b_i		: in	std_logic_vector(31 downto 0);
				syn_i	: in	std_logic;
				nxt_o	: out	std_logic_vector(7 downto 0));
	end component;
	
	component rising_edge_e is
		port(clk_i    : in std_logic;
			  rst_n_i  : in std_logic;
			  signal_i : in std_logic;
			  rising_o : out std_logic);
	end component;
	
	component falling_edge_e is
		port(clk_i    : in std_logic;
			  rst_n_i  : in std_logic;
			  signal_i : in std_logic;
			  falling_o : out std_logic);
	end component;

	signal cnta_s	: std_logic_vector(31 downto 0);
	signal cntb_s	: std_logic_vector(31 downto 0);
	signal syn_s	: std_logic;
	signal sft_s	: std_logic;
	signal syn_rising_s : std_logic;
	signal sft_falling_s : std_logic;
begin

	dualclkcnt:dualclkcnt_e
	port map(
		clka_i	=> clka_i,
		clkb_i	=> clkb_i,
		gps_i 	=> gps_i,
		rst_n_i	=> rst_n_i,
		cnta_o 	=> cnta_s,
		cntb_o 	=> cntb_s,
		syn_o 	=> syn_s );

	zwh_shift64:zwh_shift64_e
	port map(
		clk_i		=> clka_i,
		rst_n_i	=> rst_n_i,
		sft_i 	=> sft_s,
		a_i		=> cnta_s,
		b_i 		=> cntb_s,
		syn_i 	=> syn_s,
		nxt_o 	=> nxt_o);
		
	syn_rising_edge: rising_edge_e
		port map(
			clk_i 		=> clka_i,
			rst_n_i 		=> rst_n_i,
			signal_i		=> syn_s,
			rising_o		=> syn_rising_s);
			
	sft_falling_edge: falling_edge_e
		port map(
			clk_i 		=> clka_i,
			rst_n_i 		=> rst_n_i,
			signal_i		=> sft_i,
			falling_o		=> sft_falling_s);
		
	process(clka_i, rst_n_i, sft_s)
		variable sftcnt_v : unsigned(8 downto 0) := (others =>'1');
	begin
		if rst_n_i = '0' then
			sft_s <= '0';
			sftcnt_v := (others=>'1');
		elsif clka_i'event and clka_i = '1' then
			if sft_falling_s = '1' and sftcnt_v < 7 then
				sft_s <= '1';
				sftcnt_v := sftcnt_v + 1;
			elsif syn_rising_s = '1' and sftcnt_v > 6 then
				sftcnt_v := (others=>'0');
				sft_s <= '1';
			else
				sft_s <= '0';
			end if;
		end if;
		trg_o <= sft_s;
	end process;

end clkcntsrl_a;
