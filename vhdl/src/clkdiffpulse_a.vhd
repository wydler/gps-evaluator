architecture clkdiffpulse_a of clkdiffpulse_e is
    component clkdiv_e is
        port(clk_i : in std_logic;
             rst_i : in std_logic;
             clk_o : out std_logic);
    end component;

    signal ao_s, bo_s : std_logic;
    signal p_s        : std_logic;
    signal rst_s      : std_logic;
    signal t_s        : std_logic;
begin
    process
    begin
        if falling_edge(p_s) then
            rst_s <= '1';
        else
            rst_s <= rst_i;
        end if;

        wait for 10 ns;
    end process;

    div1 : entity work.clkdiv_e(sysclkdiv_a) port map (a_i, rst_s, ao_s);
    div2 : entity work.clkdiv_e(extclkdiv_a) port map (b_i, rst_s, bo_s);

    process
    begin
        p_s <= ao_s xor bo_s;
        p_o <= p_s;

        wait for 10 ns;
    end process;
end clkdiffpulse_a;