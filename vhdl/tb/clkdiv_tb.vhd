library ieee;
use ieee.std_logic_1164.all;

entity clkdiv_tb_e is
end clkdiv_tb_e;

architecture clkdiv_tb_a of clkdiv_tb_e is

component clkdiv_e
  port(clk_i, rst_i : in std_logic;
       clk_o        : out std_logic);
end component;

signal a_s, b_s   : std_logic;
signal rst_s      : std_logic;
signal ao_s, bo_s : std_logic;
signal o_s        : std_logic;

begin
  div1 : entity work.clkdiv_e(sysclkdiv_a) port map (a_s, rst_s, ao_s);
  div2 : entity work.clkdiv_e(extclkdiv_a) port map (b_s, rst_s, bo_s);

  process
  begin  
    a_s <= '0';
    wait for 5 ns;
    a_s <= '1';
    wait for 5 ns;
    
  end process;

  process
  begin  
    b_s <= '0';
    wait for 51 ns;
    b_s <= '1';
    wait for 51 ns;
    
  end process;

  process
  begin  
    o_s <= ao_s xor bo_s;
    wait for 1 ns;
    
  end process;

end clkdiv_tb_a;
