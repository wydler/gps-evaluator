architecture sysclkdiv_a of clkdiv_e is
    signal tmp_s: STD_LOGIC;
    signal cnt_s: integer range 0 to 49999 := 0;
begin
    process (rst_i, clk_i)
    begin
        if (rst_i = '1') then
            tmp_s <= '0';
            cnt_s <= 0;
        elsif rising_edge(clk_i) then
            if (cnt_s = 49999) then
                tmp_s <= NOT(tmp_s);
                cnt_s <= 0;
            else
                cnt_s <= cnt_s + 1;
            end if;
        end if;
    end process;
    
    clk_o <= tmp_s;
end sysclkdiv_a;

architecture extclkdiv_a of clkdiv_e is
    signal tmp_s: STD_LOGIC;
    signal cnt_s: integer range 0 to 4999 := 0;
begin
    process (rst_i, clk_i)
    begin
        if (rst_i = '1') then
            tmp_s <= '0';
            cnt_s <= 0;
        elsif rising_edge(clk_i) then
            if (cnt_s = 4999) then
                tmp_s <= NOT(tmp_s);
                cnt_s <= 0;
            else
                cnt_s <= cnt_s + 1;
            end if;
        end if;
    end process;
    
    clk_o <= tmp_s;
end extclkdiv_a;