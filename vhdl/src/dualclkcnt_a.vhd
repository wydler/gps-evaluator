architecture dualclkcnt_a of dualclkcnt_e is
    component cnt32_e is
        port(clk_i : in std_logic;
             rst_i : in std_logic;
             ena_i : in std_logic;
             cnt_o : out std_logic_vector(31 downto 0));
    end component;
    
    component gpsclksrc_e is
        port(clk_i		: in	std_logic;
			rst_n_i		: in	std_logic;
			gps_i		: in	std_logic;
			gpshalf_o	: out	std_logic;
			rising_o	: out	std_logic;
			falling_o	: out	std_logic);
    end component;
    
    signal cntrst_s			: std_logic;
    signal glbcntrst_s		: std_logic;
    signal gpstrg_s			: std_logic;
begin

	gpsclksrc: gpsclksrc_e
	port map(
		clk_i 		=> clka_i,
		rst_n_i 		=> rst_n_i,
		gps_i 		=> gps_i,
		gpshalf_o 	=> gpstrg_s,
		rising_o 	=> cntrst_s,
		falling_o	=> syn_o);

	sysclkcnt32:cnt32_e
	port map(
		clk_i => clka_i,
		rst_i => glbcntrst_s,
		ena_i => gpstrg_s,
		cnt_o => cnta_o);
		
	extclkcnt32:cnt32_e
	port map(
		clk_i => clkb_i,
		rst_i => glbcntrst_s,
		ena_i => gpstrg_s,
		cnt_o => cntb_o);
		
	glbcntrst_s <= cntrst_s or not(rst_n_i);
		
end dualclkcnt_a;
