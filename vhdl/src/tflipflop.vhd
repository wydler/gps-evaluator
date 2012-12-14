library ieee;
use ieee.std_logic_1164.all;

entity tff is
  port(
  		clk_i: in std_logic;
        rst_n_i: in std_logic;
        q_o: out std_logic);
end tff;

architecture behave of tff is
	signal t_s :std_logic;
begin
	process (clk_i, rst_n_i) begin
		if (rst_n_i = '0') then
			t_s <= '0';
		elsif (clk_i'event and clk_i = '1') then
			t_s <= not t_s;
		end if;
	end process;
	q_o <= t_s;
end behave;

