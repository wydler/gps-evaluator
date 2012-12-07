library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

architecture cnt32_a of cnt32_e is
begin
	process( rst_i, clk_i, ena_i )
		variable cnt_next_v:unsigned(31 downto 0) := (others =>'0');
	begin
		if rst_i = '1' then
			cnt_next_v := (others=>'0');
		elsif clk_i'event and clk_i = '1' and ena_i = '1' then
			cnt_next_v := cnt_next_v + 1;
		end if;
		cnt_o <= std_logic_vector(cnt_next_v);
	end process;
end cnt32_a;

