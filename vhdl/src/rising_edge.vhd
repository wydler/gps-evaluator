library ieee;
use ieee.std_logic_1164.all;

entity rising_edge_e is
	port(clk_i    : in std_logic;
             rst_n_i  : in std_logic;
             signal_i : in std_logic;
	     rising_o : out std_logic);
end rising_edge_e;

architecture rising_edge_a of rising_edge_e is
  
signal delay_sig_s : std_logic_vector(1 downto 0);

begin

  process(clk_i, rst_n_i)
  begin
    if (rst_n_i = '0') then
      delay_sig_s <= (others => '0');
    elsif (clk_i'event and clk_i = '1') then
      delay_sig_s(1) <= delay_sig_s(0);
      delay_sig_s(0) <= signal_i;
    end if;
  end process;
  rising_o <= (not delay_sig_s(1)) and delay_sig_s(0);

    
end rising_edge_a;
