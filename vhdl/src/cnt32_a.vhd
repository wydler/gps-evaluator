library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

architecture cnt32_a of cnt32_e is
begin
	clk_proc:process(clk_i)
		variable cnt_next_s:unsigned(31 downto 0) := (others =>'0');
	begin
		if( clk_i'event AND clk_i = '1') then
			if rst_i = '1' then
				cnt_next_s := (others =>'0');
			else
				cnt_next_s := cnt_next_s + 1;
			end if;
		end if;
		cnt_o <= std_logic_vector(cnt_next_s);
	end process clk_proc;
end cnt32_a;

