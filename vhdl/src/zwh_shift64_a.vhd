library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

architecture zwh_shift64_a of zwh_shift64_e is
	signal buf_s	: unsigned(63 downto 0);
begin
	process( rst_i, syn_i, sft_i )
		variable buf_v : unsigned(63 downto 0);
	begin
		if rst_i = '1' then
			buf_s <= (others=>'0');
			nxt_o <= (others=>'0');
		elsif syn_i'event and syn_i = '1' then
			buf_v(63 downto 32) := unsigned(b_i);
			buf_v(31 downto 0) := unsigned(a_i);
			buf_s <= buf_v;
			nxt_o <= std_logic_vector(buf_v(7 downto 0));
		elsif sft_i'event and sft_i = '1' then
			buf_s <= buf_s srl 8;
			nxt_o <= std_logic_vector(buf_s(7 downto 0));
		end if;
	end process;
end zwh_shift64_a;

