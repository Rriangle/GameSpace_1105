# MiniGame Area 資料庫架構與種子資料報告

目的：彙整 GameSpacedatabase 中 MiniGame Area 相關 20 張資料表（含 使用者／權限表格 4 張），提供欄位結構、索引／約束與指定範圍的種子資料，讓日後的 AI 任務無須直接連線 SQL Server 即能掌握資料庫設計。

- SQL Server：DESKTOP-8HQIS1S\\SQLEXPRESS
- 資料庫：GameSpacedatabase
- 生成時間：2025-11-05 08:59:13Z
- 製作規則：定義／規則／設定表格列出全部種子；其他主表僅列出 UserID 10000001 與 10000002 相關紀錄；使用者／權限表格列出全部種子。

## 使用者／權限相關表格（完整列出全部種子）

### dbo.Users
用途：儲存所有遊戲用戶帳號資訊
總筆數（資料庫）：200

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| User_ID | int | NO |  | IDENTITY(1,1) |
| User_name | nvarchar(30) | NO |  |  |
| User_Account | nvarchar(30) | NO |  |  |
| User_Password | nvarchar(255) | NO |  |  |
| User_EmailConfirmed | bit | NO | 0 |  |
| User_PhoneNumberConfirmed | bit | NO | 0 |  |
| User_TwoFactorEnabled | bit | NO | 0 |  |
| User_AccessFailedCount | int | NO | 0 |  |
| User_LockoutEnabled | bit | NO | 1 |  |
| User_LockoutEnd | datetime2(7) | YES |  |  |
| Create_Account | datetime2(0) | NO | sysdatetime() |  |

#### 索引與鍵
- **主鍵**:
  - PK__Users__206D9190FA40893F (CLUSTERED) → User_ID
- **唯一性約束／索引**:
  - UQ__Users__899F4A91E5EF8DB8 (NONCLUSTERED) → User_Account (UNIQUE CONSTRAINT)
  - UQ__Users__5F1A108682A83552 (NONCLUSTERED) → User_name (UNIQUE CONSTRAINT)
  - IX_Users_UserAccount (NONCLUSTERED) → User_Account (UNIQUE INDEX)

#### 外鍵
- 無外鍵

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出筆數：200
| User_ID | User_name | User_Account | User_Password | User_EmailConfirmed | User_PhoneNumberConfirmed | User_TwoFactorEnabled | User_AccessFailedCount | User_LockoutEnabled | User_LockoutEnd | Create_Account |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000001 | DragonKnight88 | dragonknight88 | AQAAAAIAAYagAAAAEE3RO029bdWqOjXQFJW3Wq6CBoMHDi7zbvDSt2mAy46hlTSMot0+j/UezmlYllWFdg== | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000002 | TechGuru92 | tech_guru_92 | AQAAAAIAAYagAAAAEG3KFitzgF1+7WP9fCOT6dmjPwVChzd8+P4tDLDu2G4l09L7Ucyw6UOR6Ff9unLakA== | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000003 | CoffeeAddict | coffee_addict | CoffeePwd003! | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000004 | YogaMaster | yoga_master | YogaLife004$ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000005 | BookLover | book_lover_95 | ReadMore005% | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000006 | MusicFan | music_fan_90 | MelodyPwd006^ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000007 | PhotoPro | photo_pro_87 | SnapShot007& | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000008 | GameMaster | game_master_94 | PlayTime008* | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000009 | ChefExpert | chef_expert_89 | CookWell009( | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000010 | FitnessGuru | fitness_guru_93 | StayFit010) | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000011 | TravelBlogger | travel_blogger | Explorer011- | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000012 | ArtistSoul | artist_soul_96 | Creative012= | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000013 | ScienceTeacher | science_teacher | Knowledge013+ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000014 | MovieCritic | movie_critic_85 | Cinema014[ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000015 | GardenLover | garden_lover_92 | GreenLife015] | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000016 | PetCarer | pet_carer_88 | AnimalLove016{ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000017 | TechWriter | tech_writer_91 | WriteCode017} | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000018 | FoodBlogger | food_blogger_86 | TastyFood018\| | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000019 | CarEnthusiast | car_enthusiast | FastCar019\\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000020 | LanguageTeacher | lang_teacher_90 | Polyglot020: | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000021 | WebDesigner | web_designer_93 | DesignWeb021; | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000022 | DataScientist | data_scientist | BigData022" | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000023 | SportsFan | sports_fan_87 | Champion023\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000024 | MathGenius | math_genius_94 | Numbers024< | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000025 | HistoryBuff | history_buff_89 | PastTime025> | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000026 | MusicProducer | music_producer | BeatMaker026, | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000027 | StockTrader | stock_trader_92 | BullMarket027. | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000028 | HealthCoach | health_coach_85 | Wellness028/ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000029 | AnimationArtist | anime_artist_91 | DrawToon029? | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000030 | EcoWarrior | eco_warrior_88 | SaveEarth030~ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000031 | CyberSecurity | cyber_security | Firewall031` | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000032 | VoiceActor | voice_actor_86 | SpeakOut032! | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000033 | RetailManager | retail_manager | SellWell033@ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000034 | FilmDirector | film_director | ActionCut034# | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000035 | Archaeologist | archaeologist | DigDeep035$ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000036 | WeddingPlanner | wedding_planner | PerfectDay036% | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000037 | PsychologyPhD | psychology_phd | MindStudy037^ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000038 | UrbanPlanner | urban_planner | CityDesign038 | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000039 | WineExpert | wine_expert_90 | VintageWine039 | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000040 | Nutritionist | nutritionist_93 | HealthEat040( | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000041 | Astronomer | astronomer_87 | StarGazer041) | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000042 | BalletDancer | ballet_dancer | GraceFul042- | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000043 | Economist | economist_89 | MarketForce043= | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000044 | Philosopher | philosopher_85 | DeepThink044+ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000045 | SocialWorker | social_worker | HelpOthers045[ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000046 | InteriorDesigner | interior_designer | HomeStyle046] | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000047 | TaxiDriver | taxi_driver_91 | DriveRoad047{ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000048 | Librarian | librarian_86 | BookKeeper048} | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000049 | FireFighter | fire_fighter | SaveLives049\| | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000050 | Farmer | farmer_88 | GrowCrops050\\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000051 | Journalist | journalist_92 | TruthSeeker051: | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000052 | Electrician | electrician_87 | PowerUp052; | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000053 | Veterinarian | veterinarian_90 | AnimalDoc053 | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000054 | Accountant | accountant_85 | NumberCrunch054\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000055 | Plumber | plumber_89 | FixPipes055< | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000056 | Pilot | pilot_aircraft | FlyHigh056> | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000057 | Dentist | dentist_smile_93 | TeethCare057, | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000058 | Carpenter | carpenter_wood | BuildStrong058. | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000059 | Mechanic | mechanic_auto_88 | FixEngine059/ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000060 | Pharmacist | pharmacist_med | HealthCare060? | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000061 | Engineer | engineer_civil | BuildBridge061~ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000062 | Lawyer | lawyer_justice | LegalEagle062` | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000063 | Surgeon | surgeon_medical | SaveLife063! | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000064 | Architect | architect_design | BuildDream064@ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000065 | Translator | translator_lang | CrossCulture065# | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000066 | SoftwareEngineer | software_eng_90 | CodeMaster066$ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000067 | MarketingSpec | marketing_spec | BrandBuilder067% | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000068 | ProjectManager | project_mgr_87 | ManageTeam068^ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000069 | GraphicDesigner | graphic_designer | VisualArt069& | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000070 | SalesManager | sales_manager_91 | SellMore070* | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000071 | HRSpecialist | hr_specialist | PeopleFirst071( | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000072 | FinanceAnalyst | finance_analyst | MoneyWise072) | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000073 | QualityAssurance | qa_specialist_89 | TestAll073- | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000074 | DatabaseAdmin | database_admin | DataGuard074= | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000075 | NetworkAdmin | network_admin_92 | ConnectAll075+ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000076 | SystemAnalyst | system_analyst | AnalyzeFlow076[ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000077 | UIUXDesigner | uiux_designer | UserFocus077] | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000078 | BusinessAnalyst | business_analyst | ProcessFlow078{ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000079 | DevOpsEngineer | devops_engineer | AutoDeploy079} | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000080 | SecurityExpert | security_expert | SecureAll080\| | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000081 | DataEngineer | data_engineer_94 | BigDataFlow081\\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000082 | CloudArchitect | cloud_architect | SkyCompute082: | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000083 | ProductOwner | product_owner_86 | OwnProduct083; | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000084 | ScrumMaster | scrum_master_93 | AgileWork084 | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000085 | TechnicalWriter | tech_writer_88 | DocuMaster085\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000086 | AIResearcher | ai_researcher | FutureAI086< | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000087 | BlockchainDev | blockchain_dev | CryptoCode087> | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000088 | MobileAppDev | mobile_app_dev | AppBuilder088, | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000089 | GameDeveloper | game_developer | PlayMaker089. | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000090 | RoboticsEng | robotics_eng_91 | RobotBuilder090/ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000091 | Bioinformatics | bioinformatics | LifeCode091? | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000092 | QuantAnalyst | quant_analyst | MathFinance092~ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000093 | CyberForensics | cyber_forensics | DigitalTrace093` | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000094 | MachineLearning | ml_engineer_95 | LearnMachine094! | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000095 | VRDeveloper | vr_developer_84 | VirtualWorld095@ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000096 | ARDesigner | ar_designer_92 | AugmentReal096# | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000097 | IoTEngineer | iot_engineer_89 | ConnectThings097$ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000098 | Pharmacologist | pharmacologist | DrugStudy098% | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000099 | Biotechnologist | biotech_expert | LifeTech099^ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000100 | EnvironmentalSci | env_scientist | EcoStudy100& | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000101 | GeologicalSurv | geological_surv | EarthStudy101* | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000102 | AerospaceEng | aerospace_eng_93 | SpaceTech102( | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000103 | MarineEngineer | marine_engineer | OceanTech103) | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000104 | NuclearPhysics | nuclear_physics | AtomPower104- | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000105 | ChemicalEng | chemical_eng_91 | ReactProcess105= | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000106 | MaterialSci | material_sci_86 | NewMatter106+ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000107 | OpticalEng | optical_eng_94 | LightWave107[ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000108 | AcousticEng | acoustic_eng_88 | SoundWave108] | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000109 | FluidDynamics | fluid_dynamics | FlowMotion109{ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000110 | ThermodynamicsEng | thermo_eng_90 | HeatTransfer110} | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000111 | ControlSystem | control_system | AutoControl111\| | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000112 | SignalProcessing | signal_proc_92 | WaveAnalysis112\\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000113 | PowerElectronics | power_electronics | EnergyFlow113: | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000114 | MicroElectronics | micro_electronics | TinyCircuit114; | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000115 | QuantumComputing | quantum_computing | QuantumBit115 | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000116 | NanoTechnology | nano_technology | SmallWorld116\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000117 | SolarEngineer | solar_engineer | SunPower117< | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000118 | WindEngineer | wind_engineer_95 | WindForce118> | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000119 | HydroEngineer | hydro_engineer | WaterPower119, | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000120 | GeothermalEng | geothermal_eng | EarthHeat120. | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000121 | SmartGridEng | smartgrid_eng | GridSmart121/ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000122 | EnergyStorage | energy_storage | StorePower122? | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000123 | BatteryTech | battery_tech_87 | CellPower123~ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000124 | FuelCellEng | fuel_cell_eng | CleanEnergy124` | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000125 | Geneticist | geneticist_89 | DNAExpert125! | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000126 | Biochemist | biochemist_94 | LifeChem126@ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000127 | Microbiologist | microbiologist | TinyLife127# | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000128 | Immunologist | immunologist_92 | DefenseBody128$ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000129 | Epidemiologist | epidemiologist | DiseaseTrack129% | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000130 | Neurologist | neurologist_88 | BrainDoc130^ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000131 | Cardiologist | cardiologist_91 | HeartDoc131& | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000132 | Oncologist | oncologist_86 | CancerFight132* | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000133 | Dermatologist | dermatologist | SkinCare133( | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000134 | Ophthalmologist | ophthalmologist | EyeCare134) | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000135 | Psychiatrist | psychiatrist_93 | MentalHealth135- | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000136 | Radiologist | radiologist_87 | ImageRead136= | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000137 | Anesthesiologist | anesthesiologist | PainFree137+ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000138 | Pathologist | pathologist_90 | DiagnoseTruth138[ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000139 | PhysicalTherapist | physical_therapist | MoveWell139] | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000140 | OccupationalTher | occupational_ther | WorkAbility140{ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000141 | SpeechTherapist | speech_therapist | TalkClear141} | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000142 | Chiropractor | chiropractor_89 | SpineAlign142\| | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000143 | Acupuncturist | acupuncturist | NeedleHeal143\\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000144 | MassageTherapist | massage_therapist | RelaxMuscle144 | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000145 | DietitianNutri | dietitian_nutri | EatHealthy145; | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000146 | PersonalTrainer | personal_trainer | FitBody146 | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000147 | YogaInstructor | yoga_instructor | FlexMind147\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000148 | PilatesTeacher | pilates_teacher | CoreStrength148< | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000149 | ZumbaInstructor | zumba_instructor | DanceFit149> | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000150 | SwimCoach | swim_coach_92 | WaterSport150, | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000151 | TennisCoach | tennis_coach_85 | RacketSport151. | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000152 | BasketballCoach | basketball_coach | HoopDreams152/ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000153 | SoccerCoach | soccer_coach_88 | KickGoal153? | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000154 | BaseballCoach | baseball_coach | HomeRun154~ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000155 | VolleyballCoach | volleyball_coach | NetWinner155` | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000156 | BadmintonCoach | badminton_coach | ShuttleFly156! | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000157 | TableTennisCoach | tt_coach_91 | PingPong157@ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000158 | GolfInstructor | golf_instructor | HoleInOne158# | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000159 | BoxingCoach | boxing_coach_87 | FightSport159$ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000160 | KarateInstructor | karate_instructor | MartialArt160% | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000161 | TaekwondoMaster | taekwondo_master | KickHigh161^ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000162 | JudoInstructor | judo_instructor | ThrowSkill162& | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000163 | ArcheryCoach | archery_coach_90 | BullsEye163* | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000164 | ClimbingGuide | climbing_guide | ReachTop164( | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000165 | SkiInstructor | ski_instructor | SnowSlide165) | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000166 | SurfCoach | surf_coach_93 | RideWave166- | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000167 | ScubaInstructor | scuba_instructor | DeepDive167= | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000168 | ParachuteTutor | parachute_tutor | SkydiveFun168+ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000169 | HangGlidePilot | hangglide_pilot | GlideFree169[ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000170 | BungeeOperator | bungee_operator | JumpThrill170] | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000171 | RockClimbGuide | rockclimb_guide | ClimbRock171{ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000172 | HikingGuide | hiking_guide_89 | TrailWalk172} | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000173 | CampingExpert | camping_expert | OutdoorLife173\| | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000174 | FishingGuide | fishing_guide_86 | CatchFish174\\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000175 | HuntingGuide | hunting_guide | WildHunt175: | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000176 | RaftingGuide | rafting_guide_92 | RiverRun176; | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000177 | KayakInstructor | kayak_instructor | PaddleWater177 | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000178 | CanoeGuide | canoe_guide_88 | QuietWater178\ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000179 | SailboatCaptain | sailboat_captain | WindSail179< | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000180 | YachtCaptain | yacht_captain_94 | LuxurySea180> | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000181 | CruiseDirector | cruise_director | OceanVoyage181, | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000182 | TourGuide | tour_guide_91 | ShowPlace182. | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000183 | TravelAgent | travel_agent_87 | PlanTrip183/ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000184 | EventPlanner | event_planner | PlanParty184? | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000185 | WeddingCoord | wedding_coord_85 | PerfectWed185~ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000186 | PartyOrganizer | party_organizer | FunTime186` | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000187 | CateringChef | catering_chef_93 | FeedCrowd187! | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000188 | BartenderPro | bartender_pro_89 | MixDrink188@ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000189 | SommelierWine | sommelier_wine | TasteWine189# | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000190 | BaristaExpert | barista_expert_90 | BrewCoffee190$ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000191 | PastryChef | pastry_chef_86 | SweetTreat191% | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000192 | BreadBaker | bread_baker_92 | FreshBread192^ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000193 | SushiChef | sushi_chef_88 | RawFish193& | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000194 | ItalianChef | italian_chef_94 | PastaMaster194* | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000195 | FrenchChef | french_chef_91 | CuisineArt195( | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000196 | ChineseChef | chinese_chef_87 | WokMaster196) | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000197 | JapaneseChef | japanese_chef | ZenCooking197- | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000198 | ThaiChef | thai_chef_89 | SpicyFlavor198= | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000199 | IndianChef | indian_chef_93 | CurrySpice199+ | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |
| 10000200 | MexicanChef | mexican_chef_85 | AQAAAAIAAYagAAAAEG0JMi02vLvtRUEns4sx7jOeZKSHe4YF78nQ6L9ppRR/ZtyKJqFs12TNB8XVvJSrxg== | 1 | 1 | 1 | 1 | 1 | NULL | 2025-10-23 16:14:43 |

### dbo.ManagerData
用途：儲存管理員（後台使用者）基本資訊
總筆數（資料庫）：102

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| Manager_Id | int | NO |  |  |
| Manager_Name | nvarchar(30) | YES |  |  |
| Manager_Account | varchar(30) | YES |  |  |
| Manager_Password | nvarchar(200) | YES |  |  |
| Administrator_registration_date | datetime2(7) | YES |  |  |
| Manager_Email | nvarchar(255) | NO |  |  |
| Manager_EmailConfirmed | bit | NO | 0 |  |
| Manager_AccessFailedCount | int | NO | 0 |  |
| Manager_LockoutEnabled | bit | NO | 1 |  |
| Manager_LockoutEnd | datetime2(7) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK__ManagerD__AE5FEFAD638D88FF (CLUSTERED) → Manager_Id
- **唯一性約束／索引**:
  - UQ__ManagerD__0890969EC9C76047 (NONCLUSTERED) → Manager_Email (UNIQUE CONSTRAINT)
  - UQ__ManagerD__62B5E21119A93877 (NONCLUSTERED) → Manager_Account (UNIQUE CONSTRAINT)

#### 外鍵
- 無外鍵

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出筆數：102
| Manager_Id | Manager_Name | Manager_Account | Manager_Password | Administrator_registration_date | Manager_Email | Manager_EmailConfirmed | Manager_AccessFailedCount | Manager_LockoutEnabled | Manager_LockoutEnd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30000001 | Milk Hung | zhang_zhiming_01 | AdminPass001@ | 2019-01-15 08:30:00 | zhang.zhiming@company.com | 1 | 0 | 0 | NULL |
| 30000002 | 李小華 | li_xiaohua_02 | SecurePass002# | 2019-01-16 09:15:00 | li.xiaohua@company.com | 1 | 0 | 1 | NULL |
| 30000003 | 王美玲 | wang_meiling_03 | StrongPwd003! | 2019-01-17 10:45:00 | wang.meiling@company.com | 1 | 0 | 0 | NULL |
| 30000004 | 陳大偉 | chen_dawei_04 | SafeLogin004$ | 2019-01-18 11:20:00 | chen.dawei@company.com | 1 | 0 | 1 | NULL |
| 30000005 | 林雅婷 | lin_yating_05 | Manager005% | 2019-01-19 14:30:00 | lin.yating@company.com | 1 | 2 | 1 | NULL |
| 30000006 | John Anderson | john_anderson_06 | AdminJohn006^ | 2019-01-20 15:45:00 | john.anderson@company.com | 1 | 0 | 0 | NULL |
| 30000007 | 劉建國 | liu_jianguo_07 | BuildNation007& | 2019-01-21 16:30:00 | liu.jianguo@company.com | 0 | 0 | 1 | NULL |
| 30000008 | Sarah Johnson | sarah_johnson_08 | SarahMgr008* | 2019-01-22 08:00:00 | sarah.johnson@company.com | 1 | 1 | 1 | NULL |
| 30000009 | 黃金龍 | huang_jinlong_09 | GoldenDragon009( | 2019-01-23 09:30:00 | huang.jinlong@company.com | 1 | 0 | 1 | NULL |
| 30000010 | Michael Chen | michael_chen_10 | MikeChen010) | 2019-01-24 10:15:00 | michael.chen@company.com | 1 | 0 | 1 | NULL |
| 30000011 | 趙文心 | zhao_wenxin_11 | HeartWrite011- | 2019-01-25 11:45:00 | zhao.wenxin@company.com | 0 | 3 | 1 | NULL |
| 30000012 | David Wilson | david_wilson_12 | DavidWil012= | 2019-01-26 13:20:00 | david.wilson@company.com | 1 | 0 | 1 | NULL |
| 30000013 | 吳佩君 | wu_peijun_13 | ElegantMgr013+ | 2019-01-27 14:00:00 | wu.peijun@company.com | 1 | 1 | 1 | NULL |
| 30000014 | Jennifer Liu | jennifer_liu_14 | JennyLiu014[ | 2019-01-28 15:30:00 | jennifer.liu@company.com | 1 | 0 | 1 | NULL |
| 30000015 | 許志偉 | xu_zhiwei_15 | WillPower015] | 2019-01-29 16:45:00 | xu.zhiwei@company.com | 0 | 0 | 1 | NULL |
| 30000016 | Robert Davis | robert_davis_16 | RobertD016{ | 2019-01-30 08:30:00 | robert.davis@company.com | 1 | 2 | 1 | NULL |
| 30000017 | 蔡淑芬 | cai_shufen_17 | VirtueFlower017} | 2019-01-31 09:00:00 | cai.shufen@company.com | 1 | 0 | 1 | NULL |
| 30000018 | Christopher Lee | chris_lee_18 | ChrisLee018\| | 2019-02-01 10:30:00 | chris.lee@company.com | 1 | 1 | 1 | NULL |
| 30000019 | 鄭雅琪 | zheng_yaqi_19 | ElegantQi019\\ | 2019-02-02 11:15:00 | zheng.yaqi@company.com | 0 | 0 | 1 | NULL |
| 30000020 | Matthew Brown | matthew_brown_20 | MattBrown020: | 2019-02-03 12:45:00 | matthew.brown@company.com | 1 | 0 | 1 | NULL |
| 30000021 | 楊智勇 | yang_zhiyong_21 | BraveWisdom021; | 2019-02-04 13:30:00 | yang.zhiyong@company.com | 1 | 1 | 1 | NULL |
| 30000022 | Amanda Taylor | amanda_taylor_22 | AmandaT022" | 2019-02-05 14:20:00 | amanda.taylor@company.com | 1 | 0 | 1 | NULL |
| 30000023 | 馬建華 | ma_jianhua_23 | BuildChina023\ | 2019-02-06 15:00:00 | ma.jianhua@company.com | 0 | 2 | 1 | NULL |
| 30000024 | Daniel Garcia | daniel_garcia_24 | DanielG024< | 2019-02-07 16:15:00 | daniel.garcia@company.com | 1 | 0 | 1 | NULL |
| 30000025 | 孫美珍 | sun_meizhen_25 | BeautyPearl025> | 2019-02-08 08:45:00 | sun.meizhen@company.com | 1 | 0 | 1 | NULL |
| 30000026 | Emily Rodriguez | emily_rodriguez_26 | EmilyR026, | 2019-02-09 09:30:00 | emily.rodriguez@company.com | 1 | 1 | 1 | NULL |
| 30000027 | 周文傑 | zhou_wenjie_27 | LiteraryHero027. | 2019-02-10 10:00:00 | zhou.wenjie@company.com | 0 | 0 | 1 | NULL |
| 30000028 | Anthony Martinez | anthony_martinez_28 | AnthonyM028/ | 2019-02-11 11:30:00 | anthony.martinez@company.com | 1 | 0 | 1 | NULL |
| 30000029 | 呂雅慧 | lv_yahui_29 | ElegantWisdom029? | 2019-02-12 12:15:00 | lv.yahui@company.com | 1 | 1 | 1 | NULL |
| 30000030 | Brian Thompson | brian_thompson_30 | BrianT030~ | 2019-02-13 13:45:00 | brian.thompson@company.com | 1 | 0 | 1 | NULL |
| 30000031 | 郭志強 | guo_zhiqiang_31 | StrongWill031` | 2019-02-14 14:30:00 | guo.zhiqiang@company.com | 0 | 3 | 1 | NULL |
| 30000032 | Jessica White | jessica_white_32 | JessicaW032! | 2019-02-15 15:20:00 | jessica.white@company.com | 1 | 0 | 1 | NULL |
| 30000033 | 高文斌 | gao_wenbin_33 | CultureElegance033@ | 2019-02-16 16:00:00 | gao.wenbin@company.com | 1 | 0 | 1 | NULL |
| 30000034 | Kevin Anderson | kevin_anderson_34 | KevinA034# | 2019-02-17 08:30:00 | kevin.anderson@company.com | 1 | 2 | 1 | NULL |
| 30000035 | 何美君 | he_meijun_35 | BeautyLady035$ | 2019-02-18 09:45:00 | he.meijun@company.com | 0 | 0 | 1 | NULL |
| 30000036 | Rachel Green | rachel_green_36 | RachelG036% | 2019-02-19 10:30:00 | rachel.green@company.com | 1 | 1 | 1 | NULL |
| 30000037 | 石志明 | shi_zhiming_37 | RockBright037^ | 2019-02-20 11:15:00 | shi.zhiming@company.com | 1 | 0 | 1 | NULL |
| 30000038 | Steven Clark | steven_clark_38 | StevenC038& | 2019-02-21 12:00:00 | steven.clark@company.com | 1 | 0 | 1 | NULL |
| 30000039 | 范雅玲 | fan_yaling_39 | ElegantBell039* | 2019-02-22 13:30:00 | fan.yaling@company.com | 0 | 1 | 1 | NULL |
| 30000040 | Mark Johnson | mark_johnson_40 | MarkJ040( | 2019-02-23 14:45:00 | mark.johnson@company.com | 1 | 0 | 1 | NULL |
| 30000041 | 袁志華 | yuan_zhihua_41 | ChiefFlower041) | 2019-02-24 15:30:00 | yuan.zhihua@company.com | 1 | 2 | 1 | NULL |
| 30000042 | Lisa Adams | lisa_adams_42 | LisaA042- | 2019-02-25 16:20:00 | lisa.adams@company.com | 1 | 0 | 1 | NULL |
| 30000043 | 蕭文龍 | xiao_wenlong_43 | LiteraryDragon043= | 2019-02-26 08:00:00 | xiao.wenlong@company.com | 0 | 0 | 1 | NULL |
| 30000044 | Paul Wilson | paul_wilson_44 | PaulW044+ | 2019-02-27 09:30:00 | paul.wilson@company.com | 1 | 1 | 1 | NULL |
| 30000045 | 曾美華 | zeng_meihua_45 | BeautyFlower045[ | 2019-02-28 10:15:00 | zeng.meihua@company.com | 1 | 0 | 1 | NULL |
| 30000046 | Karen Miller | karen_miller_46 | KarenM046] | 2019-03-01 11:45:00 | karen.miller@company.com | 1 | 0 | 1 | NULL |
| 30000047 | 洪志偉 | hong_zhiwei_47 | GreatAmbition047{ | 2019-03-02 12:30:00 | hong.zhiwei@company.com | 0 | 3 | 1 | NULL |
| 30000048 | Thomas Davis | thomas_davis_48 | TomDavis048} | 2019-03-03 13:15:00 | thomas.davis@company.com | 1 | 0 | 1 | NULL |
| 30000049 | 莊雅文 | zhuang_yawen_49 | ElegantCulture049\| | 2019-03-04 14:00:00 | zhuang.yawen@company.com | 1 | 1 | 1 | NULL |
| 30000050 | Jason Lee | jason_lee_50 | JasonL050\\ | 2019-03-05 15:30:00 | jason.lee@company.com | 1 | 0 | 1 | NULL |
| 30000051 | 鍾文君 | zhong_wenjun_51 | CultureNoble051: | 2019-03-06 16:45:00 | zhong.wenjun@company.com | 0 | 0 | 1 | NULL |
| 30000052 | Michelle Wong | michelle_wong_52 | MichelleW052; | 2019-03-07 08:30:00 | michelle.wong@company.com | 1 | 2 | 1 | NULL |
| 30000053 | 田志龍 | tian_zhilong_53 | FieldDragon053 | 2019-03-08 09:00:00 | tian.zhilong@company.com | 1 | 0 | 1 | NULL |
| 30000054 | Andrew Smith | andrew_smith_54 | AndrewS054\ | 2019-03-09 10:30:00 | andrew.smith@company.com | 1 | 1 | 1 | NULL |
| 30000055 | 江美琳 | jiang_meilin_55 | BeautyForest055< | 2019-03-10 11:15:00 | jiang.meilin@company.com | 0 | 0 | 1 | NULL |
| 30000056 | Ryan Garcia | ryan_garcia_56 | RyanG056> | 2019-03-11 12:45:00 | ryan.garcia@company.com | 1 | 0 | 1 | NULL |
| 30000057 | 潘志成 | pan_zhicheng_57 | AchieveSuccess057, | 2019-03-12 13:30:00 | pan.zhicheng@company.com | 1 | 1 | 1 | NULL |
| 30000058 | Nicole Brown | nicole_brown_58 | NicoleB058. | 2019-03-13 14:20:00 | nicole.brown@company.com | 1 | 0 | 1 | NULL |
| 30000059 | 余雅芳 | yu_yafang_59 | ElegantFragrance059/ | 2019-03-14 15:00:00 | yu.yafang@company.com | 0 | 2 | 1 | NULL |
| 30000060 | Patrick O\Connor | patrick_oconnor_60 | PatrickO060? | 2019-03-15 16:30:00 | patrick.oconnor@company.com | 1 | 0 | 1 | NULL |
| 30000061 | 梁文豪 | liang_wenhao_61 | LiteraryHero061~ | 2019-03-16 08:15:00 | liang.wenhao@company.com | 1 | 0 | 1 | NULL |
| 30000062 | Stephanie Taylor | stephanie_taylor_62 | StephT062` | 2019-03-17 09:45:00 | stephanie.taylor@company.com | 1 | 1 | 1 | NULL |
| 30000063 | 韓志強 | han_zhiqiang_63 | KoreanStrong063! | 2019-03-18 10:30:00 | han.zhiqiang@company.com | 0 | 0 | 1 | NULL |
| 30000064 | Jonathan Moore | jonathan_moore_64 | JonathanM064@ | 2019-03-19 11:20:00 | jonathan.moore@company.com | 1 | 0 | 1 | NULL |
| 30000065 | 唐美惠 | tang_meihui_65 | BeautyBenefit065# | 2019-03-20 12:00:00 | tang.meihui@company.com | 1 | 1 | 1 | NULL |
| 30000066 | Elizabeth White | elizabeth_white_66 | ElizabethW066$ | 2019-03-21 13:45:00 | elizabeth.white@company.com | 1 | 0 | 1 | NULL |
| 30000067 | 顏志明 | yan_zhiming_67 | ColorBright067% | 2019-03-22 14:30:00 | yan.zhiming@company.com | 0 | 3 | 1 | NULL |
| 30000068 | Alexander Kim | alexander_kim_68 | AlexKim068^ | 2019-03-23 15:15:00 | alexander.kim@company.com | 1 | 0 | 1 | NULL |
| 30000069 | 蘇雅萍 | su_yaping_69 | ElegantApple069& | 2019-03-24 16:00:00 | su.yaping@company.com | 1 | 2 | 1 | NULL |
| 30000070 | Benjamin Clark | benjamin_clark_70 | BenjaminC070* | 2019-03-25 08:45:00 | benjamin.clark@company.com | 1 | 0 | 1 | NULL |
| 30000071 | 方文傑 | fang_wenjie_71 | DirectionHero071( | 2019-03-26 09:30:00 | fang.wenjie@company.com | 0 | 0 | 1 | NULL |
| 30000072 | Victoria Scott | victoria_scott_72 | VictoriaS072) | 2019-03-27 10:20:00 | victoria.scott@company.com | 1 | 1 | 1 | NULL |
| 30000073 | 邱志華 | qiu_zhihua_73 | HillFlower073- | 2019-03-28 11:00:00 | qiu.zhihua@company.com | 1 | 0 | 1 | NULL |
| 30000074 | Gregory Turner | gregory_turner_74 | GregoryT074= | 2019-03-29 12:30:00 | gregory.turner@company.com | 1 | 0 | 1 | NULL |
| 30000075 | 涂美玲 | tu_meiling_75 | CoatBeauty075+ | 2019-03-30 13:15:00 | tu.meiling@company.com | 0 | 1 | 1 | NULL |
| 30000076 | Catherine Hall | catherine_hall_76 | CatherineH076[ | 2019-03-31 14:45:00 | catherine.hall@company.com | 1 | 0 | 1 | NULL |
| 30000077 | 盧志豪 | lu_zhihao_77 | AmbitionHero077] | 2019-04-01 15:30:00 | lu.zhihao@company.com | 1 | 2 | 1 | NULL |
| 30000078 | Douglas Young | douglas_young_78 | DouglasY078{ | 2019-04-02 16:20:00 | douglas.young@company.com | 1 | 0 | 1 | NULL |
| 30000079 | 薛雅琴 | xue_yaqin_79 | ElegantMusic079} | 2019-04-03 08:00:00 | xue.yaqin@company.com | 0 | 0 | 1 | NULL |
| 30000080 | Samuel Harris | samuel_harris_80 | SamuelH080\| | 2019-04-04 09:15:00 | samuel.harris@company.com | 1 | 1 | 1 | NULL |
| 30000081 | 傅文龍 | fu_wenlong_81 | TeachDragon081\\ | 2019-04-05 10:45:00 | fu.wenlong@company.com | 1 | 0 | 1 | NULL |
| 30000082 | Natalie Lewis | natalie_lewis_82 | NatalieL082: | 2019-04-06 11:30:00 | natalie.lewis@company.com | 1 | 0 | 1 | NULL |
| 30000083 | 謝志偉 | xie_zhiwei_83 | ThanksBrave083; | 2019-04-07 12:15:00 | xie.zhiwei@company.com | 0 | 2 | 1 | NULL |
| 30000084 | Philip Robinson | philip_robinson_84 | PhilipR084 | 2019-04-08 13:00:00 | philip.robinson@company.com | 1 | 0 | 1 | NULL |
| 30000085 | 魏美芳 | wei_meifang_85 | BeautyFragrant085\ | 2019-04-09 14:30:00 | wei.meifang@company.com | 1 | 1 | 1 | NULL |
| 30000086 | Timothy Walker | timothy_walker_86 | TimothyW086< | 2019-04-10 15:45:00 | timothy.walker@company.com | 1 | 0 | 1 | NULL |
| 30000087 | 詹志豪 | zhan_zhihao_87 | ProclaimHero087> | 2019-04-11 16:30:00 | zhan.zhihao@company.com | 0 | 0 | 1 | NULL |
| 30000088 | Melissa Adams | melissa_adams_88 | MelissaA088, | 2019-04-12 08:20:00 | melissa.adams@company.com | 1 | 3 | 1 | NULL |
| 30000089 | 羅雅慧 | luo_yahui_89 | NetWisdom089. | 2019-04-13 09:00:00 | luo.yahui@company.com | 1 | 0 | 1 | NULL |
| 30000090 | Charles Martinez | charles_martinez_90 | CharlesM090/ | 2019-04-14 10:30:00 | charles.martinez@company.com | 1 | 1 | 1 | NULL |
| 30000091 | 簡志強 | jian_zhiqiang_91 | SimpleStrong091? | 2019-04-15 11:45:00 | jian.zhiqiang@company.com | 0 | 0 | 1 | NULL |
| 30000092 | Diana Thompson | diana_thompson_92 | DianaT092~ | 2019-04-16 12:30:00 | diana.thompson@company.com | 1 | 0 | 1 | NULL |
| 30000093 | 薄文豪 | bo_wenhao_93 | ThinHero093` | 2019-04-17 13:20:00 | bo.wenhao@company.com | 1 | 2 | 1 | NULL |
| 30000094 | Nathan Garcia | nathan_garcia_94 | NathanG094! | 2019-04-18 14:00:00 | nathan.garcia@company.com | 1 | 0 | 1 | NULL |
| 30000095 | 關美珍 | guan_meizhen_95 | GatePearl095@ | 2019-04-19 15:15:00 | guan.meizhen@company.com | 0 | 1 | 1 | NULL |
| 30000096 | George Wilson | george_wilson_96 | GeorgeW096# | 2019-04-20 16:00:00 | george.wilson@company.com | 1 | 0 | 1 | NULL |
| 30000097 | 柯志明 | ke_zhiming_97 | TreeBright097$ | 2019-04-21 08:30:00 | ke.zhiming@company.com | 1 | 0 | 1 | NULL |
| 30000098 | Angela Davis | angela_davis_98 | AngelaD098% | 2019-04-22 09:45:00 | angela.davis@company.com | 1 | 1 | 1 | NULL |
| 30000099 | 曲文傑 | qu_wenjie_99 | MelodyHero099^ | 2019-04-23 10:30:00 | qu.wenjie@company.com | 1 | 0 | 0 | NULL |
| 30000100 | Kenneth Brown | kenneth_brown_100 | KennethB100& | 2019-04-24 11:15:00 | kenneth.brown@company.com | 1 | 0 | 0 | NULL |
| 30000101 | Test | 101testt11r | 101testaf2dfg | 2019-04-24 11:15:00 | 101test@gmali.com | 1 | 2 | 1 | NULL |
| 30000102 | Kulu | 5;4cl41su2 | au4a83as24 | 2019-04-24 11:15:00 | aa0953693201@gmali.com | 1 | 2 | 1 | NULL |

### dbo.ManagerRolePermission
用途：定義管理員角色的權限組合
總筆數（資料庫）：8

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| ManagerRole_Id | int | NO |  |  |
| role_name | nvarchar(50) | NO |  |  |
| AdministratorPrivilegesManagement | bit | YES |  |  |
| UserStatusManagement | bit | YES |  |  |
| ShoppingPermissionManagement | bit | YES |  |  |
| MessagePermissionManagement | bit | YES |  |  |
| Pet_Rights_Management | bit | YES |  |  |
| customer_service | bit | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK__ManagerR__C2F66D3DC40C7408 (CLUSTERED) → ManagerRole_Id

#### 外鍵
- 無外鍵

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出筆數：8
| ManagerRole_Id | role_name | AdministratorPrivilegesManagement | UserStatusManagement | ShoppingPermissionManagement | MessagePermissionManagement | Pet_Rights_Management | customer_service |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 管理者平台管理人員 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 使用者與論壇管理精理 | 0 | 1 | 0 | 1 | 0 | 1 |
| 3 | 商城與寵物管理經理 | 0 | 0 | 1 | 0 | 1 | 0 |
| 4 | 使用者平台管理人員 | 0 | 1 | 0 | 0 | 0 | 0 |
| 5 | 購物平台管理人員 | 0 | 0 | 1 | 0 | 0 | 0 |
| 6 | 論壇平台管理人員 | 0 | 0 | 0 | 1 | 0 | 0 |
| 7 | 寵物平台管理人員 | 0 | 0 | 0 | 0 | 1 | 0 |
| 8 | 客服與交友管理員 | 0 | 0 | 0 | 0 | 0 | 1 |

### dbo.ManagerRole
用途：儲存管理員的角色指派（多對一關係）
總筆數（資料庫）：102

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| Manager_Id | int | NO |  |  |
| ManagerRole_Id | int | NO |  |  |

#### 索引與鍵
- **主鍵**:
  - PK__ManagerR__6270897EA52FCCCF (CLUSTERED) → Manager_Id, ManagerRole_Id

#### 外鍵
- FK__ManagerRo__Manag__0BE6BFCF: Manager_Id → Manager_Id | 參照 dbo.ManagerData | ON UPDATE NO_ACTION / ON DELETE NO_ACTION
- FK__ManagerRo__Manag__0CDAE408: ManagerRole_Id → ManagerRole_Id | 參照 dbo.ManagerRolePermission | ON UPDATE NO_ACTION / ON DELETE NO_ACTION
- FK__ManagerRo__Manag__57A801BA: Manager_Id → Manager_Id | 參照 dbo.ManagerData | ON UPDATE NO_ACTION / ON DELETE NO_ACTION
- FK__ManagerRo__Manag__589C25F3: ManagerRole_Id → ManagerRole_Id | 參照 dbo.ManagerRolePermission | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出筆數：102
| Manager_Id | ManagerRole_Id |
| --- | --- |
| 30000001 | 1 |
| 30000002 | 2 |
| 30000003 | 3 |
| 30000004 | 4 |
| 30000005 | 5 |
| 30000006 | 6 |
| 30000007 | 7 |
| 30000008 | 8 |
| 30000009 | 4 |
| 30000010 | 2 |
| 30000011 | 3 |
| 30000012 | 4 |
| 30000013 | 5 |
| 30000014 | 6 |
| 30000015 | 7 |
| 30000016 | 8 |
| 30000017 | 6 |
| 30000018 | 2 |
| 30000019 | 3 |
| 30000020 | 4 |
| 30000021 | 5 |
| 30000022 | 6 |
| 30000023 | 7 |
| 30000024 | 8 |
| 30000025 | 6 |
| 30000026 | 6 |
| 30000027 | 7 |
| 30000028 | 8 |
| 30000029 | 5 |
| 30000030 | 6 |
| 30000031 | 7 |
| 30000032 | 8 |
| 30000033 | 7 |
| 30000034 | 6 |
| 30000035 | 6 |
| 30000036 | 4 |
| 30000037 | 5 |
| 30000038 | 6 |
| 30000039 | 7 |
| 30000040 | 8 |
| 30000041 | 5 |
| 30000042 | 5 |
| 30000043 | 3 |
| 30000044 | 5 |
| 30000045 | 5 |
| 30000046 | 5 |
| 30000047 | 5 |
| 30000048 | 5 |
| 30000049 | 5 |
| 30000050 | 5 |
| 30000051 | 5 |
| 30000052 | 3 |
| 30000053 | 5 |
| 30000054 | 5 |
| 30000055 | 5 |
| 30000056 | 5 |
| 30000057 | 5 |
| 30000058 | 3 |
| 30000059 | 5 |
| 30000060 | 5 |
| 30000061 | 5 |
| 30000062 | 6 |
| 30000063 | 7 |
| 30000064 | 8 |
| 30000065 | 5 |
| 30000066 | 4 |
| 30000067 | 5 |
| 30000068 | 4 |
| 30000069 | 5 |
| 30000070 | 6 |
| 30000071 | 7 |
| 30000072 | 8 |
| 30000073 | 4 |
| 30000074 | 5 |
| 30000075 | 4 |
| 30000076 | 4 |
| 30000077 | 5 |
| 30000078 | 6 |
| 30000079 | 7 |
| 30000080 | 8 |
| 30000081 | 5 |
| 30000082 | 6 |
| 30000083 | 7 |
| 30000084 | 4 |
| 30000085 | 5 |
| 30000086 | 6 |
| 30000087 | 7 |
| 30000088 | 8 |
| 30000089 | 8 |
| 30000090 | 6 |
| 30000091 | 7 |
| 30000092 | 4 |
| 30000093 | 5 |
| 30000094 | 6 |
| 30000095 | 7 |
| 30000096 | 8 |
| 30000097 | 7 |
| 30000098 | 6 |
| 30000099 | 2 |
| 30000100 | 8 |
| 30000101 | 5 |
| 30000102 | 6 |

## MiniGame Area 定義／規則／設定類表格（完整列出全部種子）

### dbo.CouponType
用途：定義優惠券類型和折扣規則
總筆數（資料庫）：3

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| CouponTypeID | int | NO |  | IDENTITY(1,1) |
| Name | nvarchar(50) | NO |  |  |
| DiscountType | nvarchar(20) | NO |  |  |
| DiscountValue | decimal(18,2) | YES |  |  |
| MinSpend | decimal(18,2) | YES |  |  |
| ValidFrom | datetime2(7) | NO |  |  |
| ValidTo | datetime2(7) | NO |  |  |
| PointsCost | int | NO |  |  |
| Description | nvarchar(600) | YES |  |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_CouponType (CLUSTERED) → CouponTypeID
- **唯一性約束／索引**:
  - UQ_CouponType_Name (NONCLUSTERED) → Name (UNIQUE INDEX)
- **其他索引**:
  - IX_CouponType_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- 無外鍵

#### CHECK 約束
- CK_CouponType_DiscountType: (upper(ltrim(rtrim([DiscountType])))=N'PERCENT' OR upper(ltrim(rtrim([DiscountType])))=N'AMOUNT')
- CK_CouponType_ValidRange: ([ValidFrom]<=[ValidTo])

#### 種子資料
- 匯出筆數：3
| CouponTypeID | Name | DiscountType | DiscountValue | MinSpend | ValidFrom | ValidTo | PointsCost | Description | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 免運券 | Amount | NULL | NULL | 2023-10-26 02:09:44 | 2026-06-30 23:59:59 | 10000 | 官網商城限定 | 0 | NULL | NULL | NULL |
| 2 | 全站85折 | Percent | 0.15 | 1500.00 | 2023-01-25 14:06:52 | 2026-06-30 23:59:59 | 1000 | 官網商城限定 | 0 | NULL | NULL | NULL |
| 3 | 滿$500折$50 | Amount | 50.00 | 500.00 | 2024-11-13 10:37:53 | 2026-06-30 23:59:59 | 5000 | 官網商城限定 | 0 | NULL | NULL | NULL |

### dbo.EVoucherType
用途：定義電子禮券類型和面額
總筆數（資料庫）：20

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| EVoucherTypeID | int | NO |  | IDENTITY(1,1) |
| Name | nvarchar(50) | NO |  |  |
| ValueAmount | decimal(18,2) | NO |  |  |
| ValidFrom | datetime2(7) | NO |  |  |
| ValidTo | datetime2(7) | NO |  |  |
| PointsCost | int | NO |  |  |
| TotalAvailable | int | NO |  |  |
| Description | nvarchar(600) | YES |  |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_EVoucherType (CLUSTERED) → EVoucherTypeID
- **其他索引**:
  - IX_EVoucherType_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- 無外鍵

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出筆數：20
| EVoucherTypeID | Name | ValueAmount | ValidFrom | ValidTo | PointsCost | TotalAvailable | Description | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7-11禮券$100 | 100.00 | 2024-07-24 08:01:15 | 9999-12-31 06:10:00 | 10000 | 468 | 無期限 | 0 | NULL | NULL | NULL |
| 2 | 7-11禮券$200 | 200.00 | 2025-01-08 20:24:24 | 9999-12-31 06:10:00 | 20000 | 437 | 無期限 | 0 | NULL | NULL | NULL |
| 3 | 全家禮券$100 | 100.00 | 2024-03-05 01:55:47 | 9999-12-31 06:10:00 | 10000 | 194 | 無期限 | 0 | NULL | NULL | NULL |
| 4 | 全家禮券$200 | 200.00 | 2024-03-30 16:44:49 | 9999-12-31 06:10:00 | 20000 | 438 | 無期限 | 0 | NULL | NULL | NULL |
| 5 | 7-11特選美式咖啡商品卡 | 65.00 | 2024-05-06 09:52:59 | 9999-12-31 06:10:00 | 6500 | 433 | 無期限/冷熱任選 | 0 | NULL | NULL | NULL |
| 6 | 7-11特選拿鐵咖啡商品卡 | 80.00 | 2024-03-20 17:44:03 | 9999-12-31 06:10:00 | 8000 | 268 | 無期限/冷熱任選 | 0 | NULL | NULL | NULL |
| 7 | 威秀影城電影票 | 360.00 | 2023-06-14 09:27:37 | 9999-12-31 06:10:00 | 36000 | 356 | 無期限/平假日適用 | 0 | NULL | NULL | NULL |
| 8 | 王牌映畫影城電影票 | 200.00 | 2024-06-30 16:01:28 | 9999-12-31 06:10:00 | 20000 | 253 | 無期限/平假日適用 | 0 | NULL | NULL | NULL |
| 9 | SOGO百貨禮券$200 | 200.00 | 2023-12-08 18:22:33 | 9999-12-31 06:10:00 | 20000 | 419 | 無期限 | 0 | NULL | NULL | NULL |
| 10 | 麥當勞大麥克即享券 | 78.00 | 2024-01-14 00:08:47 | 9999-12-31 06:10:00 | 7800 | 296 | 無期限 | 0 | NULL | NULL | NULL |
| 11 | 肯德基咔啦雞腿堡＋原味蛋撻即享券 | 151.00 | 2024-04-14 13:37:46 | 9999-12-31 06:10:00 | 15100 | 234 | 無期限 | 0 | NULL | NULL | NULL |
| 12 | 必勝客六吋個人鬆厚比薩即享券 | 82.00 | 2024-09-12 17:42:59 | 9999-12-31 06:10:00 | 8200 | 452 | 無期限 | 0 | NULL | NULL | NULL |
| 13 | 星巴克大杯那堤即享券 | 140.00 | 2024-06-06 18:58:04 | 9999-12-31 06:10:00 | 14000 | 175 | 無期限/冷熱任選 | 0 | NULL | NULL | NULL |
| 14 | 摩斯漢堡蜜汁烤雞堡＋冰紅茶(L)即享券 | 130.00 | 2025-07-05 10:21:00 | 9999-12-31 06:10:00 | 13000 | 176 | 無期限 | 0 | NULL | NULL | NULL |
| 15 | 哈根達斯單球冰淇淋喜客券 | 145.00 | 2025-07-24 05:42:09 | 9999-12-31 06:10:00 | 14500 | 438 | 無期限 | 0 | NULL | NULL | NULL |
| 16 | Mister Donut甜甜圈(一入)即享券 | 42.00 | 2023-04-08 20:36:12 | 9999-12-31 06:10:00 | 4200 | 361 | 無期限/口味任選 | 0 | NULL | NULL | NULL |
| 17 | COLD STONE冰淇淋雙球好禮即享券 | 120.00 | 2023-05-12 19:35:25 | 9999-12-31 06:10:00 | 12000 | 153 | 無期限/口味任選 | 0 | NULL | NULL | NULL |
| 18 | 誠品生活禮券$200 | 200.00 | 2023-02-18 15:06:24 | 9999-12-31 06:10:00 | 20000 | 321 | 無期限 | 0 | NULL | NULL | NULL |
| 19 | 家樂福禮券$100 | 100.00 | 2024-03-26 10:04:43 | 9999-12-31 06:10:00 | 10000 | 316 | 無期限 | 0 | NULL | NULL | NULL |
| 20 | 屈臣氏禮券$200 | 200.00 | 2025-06-11 12:47:47 | 9999-12-31 06:10:00 | 20000 | 317 | 無期限 | 0 | NULL | NULL | NULL |

### dbo.PetBackgroundCostSettings
用途：定義寵物背景購買成本
總筆數（資料庫）：11

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| SettingId | int | NO |  | IDENTITY(1,1) |
| BackgroundCode | nvarchar(50) | NO |  |  |
| BackgroundName | nvarchar(100) | NO |  |  |
| PointsCost | int | NO |  |  |
| Description | nvarchar(500) | YES |  |  |
| PreviewImagePath | nvarchar(200) | YES |  |  |
| IsActive | bit | NO | 1 |  |
| DisplayOrder | int | YES | 0 |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |
| CreatedAt | datetime2(7) | NO | sysutcdatetime() |  |
| UpdatedAt | datetime2(7) | YES |  |  |
| UpdatedBy | int | YES |  |  |
| Rarity | nvarchar(20) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK__PetBackg__54372B1D7E12EEE3 (CLUSTERED) → SettingId
- **唯一性約束／索引**:
  - UQ_PetBackgroundCostSettings_BackgroundCode (NONCLUSTERED) → BackgroundCode (UNIQUE CONSTRAINT)

#### 外鍵
- FK_PetBackgroundCostSettings_UpdatedBy_Manager: UpdatedBy → Manager_Id | 參照 dbo.ManagerData | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- CK__PetBackgr__Point__541767F8: ([PointsCost]>=(0))

#### 種子資料
- 匯出筆數：11
| SettingId | BackgroundCode | BackgroundName | PointsCost | Description | PreviewImagePath | IsActive | DisplayOrder | IsDeleted | DeletedAt | DeletedBy | DeleteReason | CreatedAt | UpdatedAt | UpdatedBy | Rarity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19 | BG001 | 萬聖南瓜 | 0 | 充滿萬聖節氣氛的南瓜場景，神秘又可愛 | /images/backgrounds/halloween-pumpkin.jpg | 1 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 普通 |
| 20 | BG002 | 彩窗教堂 | 0 | 神聖莊嚴的彩繪玻璃教堂，光影交錯如夢似幻 | /images/backgrounds/stained-glass-church.jpg | 1 | 2 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 普通 |
| 21 | BG003 | 珊瑚海灘 | 0 | 熱帶珊瑚海灘，碧海藍天令人心曠神怡 | /images/backgrounds/coral-beach.jpg | 1 | 3 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 普通 |
| 22 | BG004 | 清新森林 | 2000 | 陽光灑落的清新森林，鳥語花香 | /images/backgrounds/fresh-forest.jpg | 1 | 4 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 普通 |
| 23 | BG005 | 雨林瀑布 | 2500 | 熱帶雨林深處的壯觀瀑布，生機盎然 | /images/backgrounds/rainforest-waterfall.jpg | 1 | 5 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 普通 |
| 24 | BG006 | 清晨教室 | 3000 | 清晨陽光照進的日式教室，寧靜溫馨 | /images/backgrounds/morning-classroom.jpg | 1 | 6 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 普通 |
| 25 | BG007 | 霓虹天際 | 3500 | 未來都市的霓虹夜景，賽博龐克風格 | /images/backgrounds/neon-skyline.jpg | 1 | 7 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 普通 |
| 26 | BG008 | 極光雪原 | 4000 | 極地夜空下的絢爛極光，冰雪世界的奇景 | /images/backgrounds/aurora-snowfield.jpg | 1 | 8 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 普通 |
| 27 | BG009 | 魔法書庫 | 4500 | 古老魔法書庫，充滿神秘魔力的知識殿堂 | /images/backgrounds/magic-library.jpg | 1 | 9 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 稀有 |
| 28 | BG010 | 地獄熔岩 | 6000 | 地獄深處的熔岩火海，危險而震撼 | /images/backgrounds/hell-lava.jpg | 1 | 10 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:39.028297 | NULL | NULL | 稀有 |
| 29 | BG011 | 蒸汽工坊 | 2000 | 工業革命時代的蒸汽機械工坊（已下架） | /images/backgrounds/steam-workshop.jpg | 0 | 11 | 1 | 2025-10-23 10:33:39.028297 | NULL | 背景內容不符合當前主題，已下架 | 2025-10-23 10:33:39.028297 | NULL | NULL | 活動 |

### dbo.PetSkinColorCostSettings
用途：定義寵物膚色購買成本
總筆數（資料庫）：11

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| SettingId | int | NO |  | IDENTITY(1,1) |
| ColorCode | varchar(10) | NO |  |  |
| ColorName | nvarchar(50) | NO |  |  |
| PointsCost | int | NO | 2000 |  |
| Rarity | nvarchar(20) | NO | N'普通' |  |
| Description | nvarchar(500) | YES |  |  |
| PreviewImagePath | nvarchar(500) | YES |  |  |
| ColorHex | varchar(7) | YES |  |  |
| IsActive | bit | NO | 1 |  |
| DisplayOrder | int | NO | 0 |  |
| IsFree | bit | NO | 0 |  |
| IsLimitedEdition | bit | NO | 0 |  |
| AvailableFrom | datetime2(7) | YES |  |  |
| AvailableUntil | datetime2(7) | YES |  |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |
| CreatedAt | datetime2(7) | NO | sysutcdatetime() |  |
| UpdatedAt | datetime2(7) | YES |  |  |
| UpdatedBy | int | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_PetSkinColorCostSettings (CLUSTERED) → SettingId
- **唯一性約束／索引**:
  - UQ_PetSkinColorCostSettings_ColorCode (NONCLUSTERED) → ColorCode (UNIQUE CONSTRAINT)
- **其他索引**:
  - IX_PetSkinColorCostSettings_IsActive_DisplayOrder (NONCLUSTERED) → IsActive, DisplayOrder | Filter: ([IsDeleted]=(0))
  - IX_PetSkinColorCostSettings_Rarity (NONCLUSTERED) → Rarity | Filter: ([IsDeleted]=(0) AND [IsActive]=(1))

#### 外鍵
- 無外鍵

#### CHECK 約束
- CK_PetSkinColorCostSettings_ColorCode: ([ColorCode] like '#%' AND len([ColorCode])>=(4))
- CK_PetSkinColorCostSettings_PointsCost: ([PointsCost]>=(0))
- CK_PetSkinColorCostSettings_Rarity: ([Rarity]=N'活動' OR [Rarity]=N'限定' OR [Rarity]=N'傳說' OR [Rarity]=N'稀有' OR [Rarity]=N'普通')

#### 種子資料
- 匯出筆數：11
| SettingId | ColorCode | ColorName | PointsCost | Rarity | Description | PreviewImagePath | ColorHex | IsActive | DisplayOrder | IsFree | IsLimitedEdition | AvailableFrom | AvailableUntil | IsDeleted | DeletedAt | DeletedBy | DeleteReason | CreatedAt | UpdatedAt | UpdatedBy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | #FFFFFF | 白色 | 0 | 普通 | 純淨的白色，經典基礎色 | NULL | NULL | 1 | 1 | 1 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 2 | #000000 | 黑色 | 0 | 普通 | 神秘的黑色，經典基礎色 | NULL | NULL | 1 | 2 | 1 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 3 | #FF0000 | 紅色 | 0 | 普通 | 熱情的紅色，經典基礎色 | NULL | NULL | 1 | 3 | 1 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 4 | #FFA500 | 橙色 | 2000 | 普通 | 溫暖活潑的橙色 | NULL | NULL | 1 | 10 | 0 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 5 | #FFFF00 | 黃色 | 2000 | 普通 | 明亮開朗的黃色 | NULL | NULL | 1 | 11 | 0 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 6 | #008000 | 綠色 | 2000 | 普通 | 生機盎然的綠色 | NULL | NULL | 1 | 12 | 0 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 7 | #00FFFF | 青色 | 2000 | 普通 | 清爽透徹的青色 | NULL | NULL | 1 | 13 | 0 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 8 | #0000FF | 藍色 | 2000 | 普通 | 深邃沉穩的藍色 | NULL | NULL | 1 | 14 | 0 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 9 | #800080 | 紫色 | 3500 | 稀有 | 高貴神秘的紫色 | NULL | NULL | 1 | 30 | 0 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 10 | #6F4E37 | 咖啡色 | 3500 | 稀有 | 溫潤厚實的咖啡色 | NULL | NULL | 1 | 31 | 0 | 0 | NULL | NULL | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.911002 | NULL | NULL |
| 11 | #6EFE19 | 螢光綠 | 2000 | 活動 | 限時活動顏色（已下架） | NULL | NULL | 0 | 99 | 0 | 0 | NULL | NULL | 1 | 2025-10-23 10:33:38.911002 | NULL | 活動結束，顏色過於刺眼，已下架 | 2025-10-23 10:33:38.911002 | NULL | NULL |

### dbo.PetLevelRewardSettings
用途：定義寵物升級獎勵規則
總筆數（資料庫）：25

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| SettingId | int | NO |  | IDENTITY(1,1) |
| LevelRangeStart | int | NO |  |  |
| LevelRangeEnd | int | NO |  |  |
| PointsReward | int | NO |  |  |
| Description | nvarchar(500) | YES |  |  |
| IsActive | bit | NO | 1 |  |
| DisplayOrder | int | NO | 0 |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |
| CreatedAt | datetime2(7) | NO | sysutcdatetime() |  |
| UpdatedAt | datetime2(7) | YES |  |  |
| UpdatedBy | int | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_PetLevelRewardSettings (CLUSTERED) → SettingId
- **唯一性約束／索引**:
  - UQ_PetLevelRewardSettings_LevelRange (NONCLUSTERED) → LevelRangeStart, LevelRangeEnd (UNIQUE CONSTRAINT)
- **其他索引**:
  - IX_PetLevelRewardSettings_LevelRange (NONCLUSTERED) → LevelRangeStart, LevelRangeEnd | Filter: ([IsDeleted]=(0) AND [IsActive]=(1))

#### 外鍵
- 無外鍵

#### CHECK 約束
- CK_PetLevelRewardSettings_LevelRange: ([LevelRangeStart]>(0) AND [LevelRangeEnd]>=[LevelRangeStart])
- CK_PetLevelRewardSettings_PointsReward: ([PointsReward]>=(0) AND [PointsReward]<=(999999))

#### 種子資料
- 匯出筆數：25
| SettingId | LevelRangeStart | LevelRangeEnd | PointsReward | Description | IsActive | DisplayOrder | IsDeleted | DeletedAt | DeletedBy | DeleteReason | CreatedAt | UpdatedAt | UpdatedBy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 10 | 10 | 初級獎勵（Level 1-10） | 1 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 2 | 11 | 20 | 20 | 進階獎勵（Level 11-20） | 1 | 2 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 3 | 21 | 30 | 30 | 中級獎勵（Level 21-30） | 1 | 3 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 4 | 31 | 40 | 40 | 高級獎勵（Level 31-40） | 1 | 4 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 5 | 41 | 50 | 50 | 精英獎勵（Level 41-50） | 1 | 5 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 6 | 51 | 60 | 60 | 專家獎勵（Level 51-60） | 1 | 6 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 7 | 61 | 70 | 70 | 大師獎勵（Level 61-70） | 1 | 7 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 8 | 71 | 80 | 80 | 宗師獎勵（Level 71-80） | 1 | 8 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 9 | 81 | 90 | 90 | 傳奇獎勵（Level 81-90） | 1 | 9 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 10 | 91 | 100 | 100 | 史詩獎勵（Level 91-100） | 1 | 10 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 11 | 101 | 110 | 110 | 神話獎勵（Level 101-110） | 1 | 11 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 12 | 111 | 120 | 120 | 不朽獎勵（Level 111-120） | 1 | 12 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 13 | 121 | 130 | 130 | 永恆獎勵（Level 121-130） | 1 | 13 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 14 | 131 | 140 | 140 | 至尊獎勵（Level 131-140） | 1 | 14 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 15 | 141 | 150 | 150 | 無上獎勵（Level 141-150） | 1 | 15 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 16 | 151 | 160 | 160 | 天域獎勵（Level 151-160） | 1 | 16 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 17 | 161 | 170 | 170 | 聖域獎勵（Level 161-170） | 1 | 17 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 18 | 171 | 180 | 180 | 神域獎勵（Level 171-180） | 1 | 18 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 19 | 181 | 190 | 190 | 魔域獎勵（Level 181-190） | 1 | 19 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 20 | 191 | 200 | 200 | 仙域獎勵（Level 191-200） | 1 | 20 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 21 | 201 | 210 | 210 | 帝域獎勵（Level 201-210） | 1 | 21 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 22 | 211 | 220 | 220 | 皇域獎勵（Level 211-220） | 1 | 22 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 23 | 221 | 230 | 230 | 王域獎勵（Level 221-230） | 1 | 23 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 24 | 231 | 240 | 240 | 霸域獎勵（Level 231-240） | 1 | 24 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |
| 25 | 241 | 250 | 250 | 極限獎勵（Level 241-250，上限） | 1 | 25 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.929848 | NULL | NULL |

### dbo.SignInRule
用途：定義簽到獎勵規則
總筆數（資料庫）：10

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| Id | int | NO |  | IDENTITY(1,1) |
| SignInDay | int | NO |  |  |
| Points | int | NO |  |  |
| Experience | int | NO |  |  |
| HasCoupon | bit | NO | 0 |  |
| CouponTypeCode | nvarchar(50) | YES |  |  |
| IsActive | bit | NO | 1 |  |
| CreatedAt | datetime2(7) | NO | sysutcdatetime() |  |
| UpdatedAt | datetime2(7) | YES |  |  |
| Description | nvarchar(255) | YES |  |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_SignInRule (CLUSTERED) → Id
- **唯一性約束／索引**:
  - UQ_SignInRule_SignInDay_Active (NONCLUSTERED) → SignInDay | Filter: ([IsActive]=(1)) (UNIQUE INDEX)
- **其他索引**:
  - IX_SignInRule_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_SignInRule_CouponType_Name: CouponTypeCode → Name | 參照 dbo.CouponType | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- CK_SignInRule_CouponFlag: ([HasCoupon]=(1) AND [CouponTypeCode] IS NOT NULL OR [HasCoupon]=(0) AND [CouponTypeCode] IS NULL)
- CK_SignInRule_DayRange: ([SignInDay]>=(1) AND [SignInDay]<=(365))
- CK_SignInRule_Positive: ([Points]>=(0) AND [Experience]>=(0))

#### 種子資料
- 匯出筆數：10
| Id | SignInDay | Points | Experience | HasCoupon | CouponTypeCode | IsActive | CreatedAt | UpdatedAt | Description | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 20 | 0 | 0 | NULL | 1 | 2025-10-23 10:32:52.096102 | 2025-10-23 10:33:23.40802 | 第 1 天簽到獎勵 | 0 | NULL | NULL | NULL |
| 2 | 2 | 20 | 0 | 0 | NULL | 1 | 2025-10-23 10:32:52.096102 | 2025-10-23 10:33:23.40802 | 第 2 天簽到獎勵 | 0 | NULL | NULL | NULL |
| 3 | 3 | 20 | 0 | 0 | NULL | 1 | 2025-10-23 10:32:52.096102 | 2025-10-23 10:33:23.40802 | 第 3 天簽到獎勵 | 0 | NULL | NULL | NULL |
| 4 | 4 | 20 | 0 | 0 | NULL | 1 | 2025-10-23 10:32:52.096102 | 2025-10-23 10:33:23.40802 | 第 4 天簽到獎勵 | 0 | NULL | NULL | NULL |
| 5 | 5 | 20 | 0 | 0 | NULL | 1 | 2025-10-23 10:32:52.096102 | 2025-10-23 10:33:23.40802 | 第 5 天簽到獎勵 | 0 | NULL | NULL | NULL |
| 6 | 6 | 30 | 200 | 0 | NULL | 1 | 2025-10-23 10:32:52.096102 | 2025-10-23 10:33:23.410158 | 第 6 天簽到獎勵 | 0 | NULL | NULL | NULL |
| 7 | 7 | 70 | 500 | 0 | NULL | 1 | 2025-10-23 10:32:52.096102 | 2025-10-23 10:33:23.412493 | 第 7 天簽到獎勵 + 週獎勵券 | 0 | NULL | NULL | NULL |
| 11 | 14 | 0 | 0 | 0 | NULL | 1 | 2025-10-23 10:33:40.049851 | NULL | 連續簽到 14 天獎勵優惠券 | 0 | NULL | NULL | NULL |
| 12 | 21 | 0 | 0 | 0 | NULL | 1 | 2025-10-23 10:33:40.05085 | NULL | 連續簽到 21 天獎勵優惠券 | 0 | NULL | NULL | NULL |
| 10 | 30 | 200 | 2000 | 0 | NULL | 1 | 2025-10-23 10:32:52.096102 | 2025-10-23 10:33:23.419983 | 連續簽到 30 天獎勵（含大獎） | 0 | NULL | NULL | NULL |

### dbo.SystemSettings
用途：動態配置中心，存儲系統參數
總筆數（資料庫）：56

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| SettingId | int | NO |  | IDENTITY(1,1) |
| SettingKey | nvarchar(200) | NO |  |  |
| SettingValue | nvarchar(max) | YES |  |  |
| Description | nvarchar(500) | YES |  |  |
| Category | nvarchar(100) | NO | 'General' |  |
| SettingType | nvarchar(50) | NO | 'String' |  |
| IsReadOnly | bit | NO | 0 |  |
| IsActive | bit | NO | 1 |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |
| CreatedAt | datetime2(7) | NO | sysutcdatetime() |  |
| UpdatedAt | datetime2(7) | YES |  |  |
| UpdatedBy | int | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK__SystemSe__54372B1D4E2C6147 (CLUSTERED) → SettingId
- **唯一性約束／索引**:
  - UQ_SystemSettings_SettingKey (NONCLUSTERED) → SettingKey (UNIQUE CONSTRAINT)

#### 外鍵
- FK_SystemSettings_UpdatedBy_Manager: UpdatedBy → Manager_Id | 參照 dbo.ManagerData | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- CHK_SystemSettings_SettingType: ([SettingType]='String' OR [SettingType]='Boolean' OR [SettingType]='Number' OR [SettingType]='JSON')

#### 種子資料
- 匯出筆數：56
| SettingId | SettingKey | SettingValue | Description | Category | SettingType | IsReadOnly | IsActive | IsDeleted | DeletedAt | DeletedBy | DeleteReason | CreatedAt | UpdatedAt | UpdatedBy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Game.DefaultDailyLimit | 3 | Default daily game limit | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 2 | Game.Levels.Configuration | {"levels":[{"level":1,"monsterCount":6,"speedMultiplier":1.0,"experienceReward":100,"pointsReward":10,"hasCoupon":false},{"level":2,"monsterCount":8,"speedMultiplier":1.5,"experienceReward":200,"pointsReward":20,"hasCoupon":false},{"level":3,"monsterCount":10,"speedMultiplier":2.0,"experienceReward":300,"pointsReward":30,"hasCoupon":true,"couponType":"LEVEL_3_COMPLETION"}]} | Game level configuration (3 levels) | Game | JSON | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 3 | Game.Level1.MonsterCount | 6 | Level 1 monster count | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 4 | Game.Level2.MonsterCount | 8 | Level 2 monster count | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 5 | Game.Level3.MonsterCount | 10 | Level 3 monster count | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 6 | Game.Level1.SpeedMultiplier | 1.0 | Level 1 speed multiplier | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 7 | Game.Level2.SpeedMultiplier | 1.5 | Level 2 speed multiplier | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 8 | Game.Level3.SpeedMultiplier | 2.0 | Level 3 speed multiplier | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 9 | Game.Level1.ExperienceReward | 100 | Level 1 completion experience reward | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 10 | Game.Level2.ExperienceReward | 200 | Level 2 completion experience reward | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 11 | Game.Level3.ExperienceReward | 300 | Level 3 completion experience reward | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 12 | Game.Level1.PointsReward | 10 | Level 1 completion points reward | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 13 | Game.Level2.PointsReward | 20 | Level 2 completion points reward | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 14 | Game.Level3.PointsReward | 30 | Level 3 completion points reward | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 15 | Pet.Interaction.Feed.HungerIncrease | 10 | Feed increases hunger | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 16 | Pet.Interaction.Feed.HealthIncrease | 10 | Feed increases health | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 17 | Pet.Interaction.Bath.CleanlinessIncrease | 10 | Bath increases cleanliness | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 18 | Pet.Interaction.Bath.MoodIncrease | 10 | Bath increases mood | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 19 | Pet.Interaction.Coax.MoodIncrease | 10 | Coax increases mood | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 20 | Pet.Interaction.Coax.StaminaIncrease | 10 | Coax increases stamina | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 21 | Pet.Interaction.Rest.StaminaIncrease | 10 | Rest increases stamina | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 22 | Pet.Interaction.Rest.HealthIncrease | 10 | Rest increases health | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 23 | Pet.DailyDecay.HungerDecay | 20 | Daily hunger decay | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 24 | Pet.DailyDecay.MoodDecay | 30 | Daily mood decay | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 25 | Pet.DailyDecay.StaminaDecay | 10 | Daily stamina decay | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 26 | Pet.DailyDecay.CleanlinessDecay | 20 | Daily cleanliness decay | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 27 | Pet.DailyDecay.HealthDecay | 0 | Daily health decay (no decay) | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 28 | Pet.ColorChange.PointsCost | 2000 | Pet color change points cost | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 29 | Pet.DailyFullStatsBonus.Experience | 100 | Daily full stats bonus experience | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 30 | Pet.DailyFullStatsBonus.Points | 0 | Daily full stats bonus points (no bonus) | Pet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 31 | Pet.LevelUp.Formula | {
  "description": "Pet level-up experience formula (2025-10-20 updated)",
  "tiers": [
    {
      "minLevel": 1,
      "maxLevel": 10,
      "type": "linear",
      "formula": "40 * level + 60",
      "description": "Level 1-10: EXP = 40 × level + 60"
    },
    {
      "minLevel": 11,
      "maxLevel": 100,
      "type": "quadratic",
      "formula": "0.8 * level^2 + 380",
      "description": "Level 11-100: EXP = 0.8 × level2 + 380"
    },
    {
      "minLevel": 101,
      "maxLevel": 250,
      "type": "exponential",
      "formula": "285.69 * (1.06^level)",
      "description": "Level ? 101: EXP = 285.69 × (1.06^level)"
    }
  ]
} | Pet level up experience formula (3 tiers) | Pet | JSON | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | 2025-10-23 10:33:39.616101 | NULL |
| 32 | SignIn.Weekday.Points | 20 | Weekday sign-in points reward | SignIn | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 33 | SignIn.Weekday.Experience | 0 | Weekday sign-in experience reward | SignIn | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 34 | SignIn.Weekend.Points | 30 | Weekend sign-in points reward | SignIn | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 35 | SignIn.Weekend.Experience | 200 | Weekend sign-in experience reward | SignIn | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 36 | SignIn.Streak7Days.BonusPoints | 40 | Consecutive 7 days extra points reward | SignIn | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 37 | SignIn.Streak7Days.BonusExperience | 300 | Consecutive 7 days extra experience reward | SignIn | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 38 | SignIn.Streak7Days.HasCoupon | false | Consecutive 7 days no coupon | SignIn | Boolean | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 39 | SignIn.PerfectAttendance30Days.BonusPoints | 200 | Perfect attendance extra points reward | SignIn | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 40 | SignIn.PerfectAttendance30Days.BonusExperience | 2000 | Perfect attendance extra experience reward | SignIn | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 41 | SignIn.PerfectAttendance30Days.HasCoupon | true | Perfect attendance issue coupon | SignIn | Boolean | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 42 | SignIn.PerfectAttendance30Days.CouponType | MONTH_BONUS | Perfect attendance coupon type | SignIn | String | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 43 | Wallet.MaxPoints | 999999 | Maximum points limit | Wallet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 44 | Wallet.InitialPoints | 1000 | New user initial points | Wallet | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 45 | Coupon.DefaultValidityDays | 30 | Coupon default validity days | Coupon | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 46 | EVoucher.DefaultValidityDays | 90 | E-voucher default validity days | EVoucher | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:23.321845 | NULL | NULL |
| 47 | Game.Result.Win.HungerDelta | -20 | Game win hunger delta | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.945346 | NULL | NULL |
| 48 | Game.Result.Win.MoodDelta | 30 | Game win mood delta | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.946849 | NULL | NULL |
| 49 | Game.Result.Win.StaminaDelta | -20 | Game win stamina delta | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.946849 | NULL | NULL |
| 50 | Game.Result.Win.CleanlinessDelta | -20 | Game win cleanliness delta | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.946849 | NULL | NULL |
| 51 | Game.Result.Lose.HungerDelta | -20 | Game lose hunger delta | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.946849 | NULL | NULL |
| 52 | Game.Result.Lose.MoodDelta | -30 | Game lose mood delta | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.947857 | NULL | NULL |
| 53 | Game.Result.Lose.StaminaDelta | -20 | Game lose stamina delta | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.947857 | NULL | NULL |
| 54 | Game.Result.Lose.CleanlinessDelta | -20 | Game lose cleanliness delta | Game | Number | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.947857 | NULL | NULL |
| 55 | Game.Level3.HasCoupon | true | Level 3 completion issue coupon | Game | Boolean | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.947857 | NULL | NULL |
| 56 | Game.Level3.CouponType | GAME_LEVEL3_BONUS | Level 3 completion coupon type | Game | String | 0 | 1 | 0 | NULL | NULL | NULL | 2025-10-23 10:33:38.947857 | NULL | NULL |

## MiniGame Area 使用者相關表格（僅列出 UserID 10000001 與 10000002）

### dbo.Coupon
用途：儲存會員優惠券所有權
總筆數（資料庫）：4566

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| CouponID | int | NO |  | IDENTITY(1,1) |
| CouponCode | nvarchar(50) | NO |  |  |
| CouponTypeID | int | NO |  |  |
| UserID | int | NO |  |  |
| IsUsed | bit | NO |  |  |
| AcquiredTime | datetime2(7) | NO | sysutcdatetime() |  |
| UsedTime | datetime2(7) | YES | sysutcdatetime() |  |
| UsedInOrderID | int | YES |  |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_Coupon (CLUSTERED) → CouponID
- **唯一性約束／索引**:
  - UQ_Coupon_CouponCode (NONCLUSTERED) → CouponCode (UNIQUE CONSTRAINT)
- **其他索引**:
  - IX_Coupon_user_used (NONCLUSTERED) → UserID, IsUsed, AcquiredTime
  - IX_Coupon_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_Coupon_CouponType: CouponTypeID → CouponTypeID | 參照 dbo.CouponType | ON UPDATE NO_ACTION / ON DELETE NO_ACTION
- FK_Coupon_Users: UserID → User_ID | 參照 dbo.Users | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- CK_Coupon_IsUsed: ([IsUsed]=(1) OR [IsUsed]=(0))
- CK_Coupon_UsedFields: ([IsUsed]=(0) AND [UsedTime] IS NULL AND [UsedInOrderID] IS NULL OR [IsUsed]=(1) AND [UsedTime] IS NOT NULL AND [UsedInOrderID] IS NOT NULL)

#### 種子資料
- 匯出條件：UserID ∈ {10000001, 10000002}
- 匯出筆數：24
- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。
| CouponID | CouponCode | CouponTypeID | UserID | IsUsed | AcquiredTime | UsedTime | UsedInOrderID | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5964 | CPN-2503-MG1029 | 3 | 10000001 | 0 | 2025-03-04 04:52:49 | NULL | NULL | 0 | NULL | NULL | NULL |
| 5979 | CPN-2308-MG1044 | 3 | 10000001 | 0 | 2023-08-26 04:13:03 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9180 | CPN-2302-HCA748 | 1 | 10000001 | 0 | 2024-06-19 06:36:51 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9423 | CPN-2401-A7B2K9 | 1 | 10000001 | 0 | 2024-01-21 09:45:18 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9424 | CPN-2402-XW4H8P | 1 | 10000001 | 0 | 2024-02-01 08:44:28 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9425 | CPN-2402-M9N5QT | 2 | 10000001 | 0 | 2024-02-08 08:31:45 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9426 | CPN-2402-R3V7CJ | 1 | 10000001 | 0 | 2024-02-19 08:22:48 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9427 | CPN-2402-FG6Y2L | 2 | 10000001 | 0 | 2024-02-26 08:17:45 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9428 | CPN-2403-ZK8D4W | 3 | 10000001 | 0 | 2024-03-04 08:24:37 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9502 | CPN-2506-WJ9F2T | 1 | 10000001 | 0 | 2025-06-30 11:05:33 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9509 | CPN-2403-BQ8N4R | 1 | 10000001 | 0 | 2024-03-08 10:07:56 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9511 | CPN-2312-HG7K3M | 1 | 10000001 | 0 | 2023-12-01 20:41:09 | NULL | NULL | 0 | NULL | NULL | NULL |
| 6058 | CPN-2404-MG1123 | 3 | 10000002 | 0 | 2024-04-22 07:34:48 | NULL | NULL | 0 | NULL | NULL | NULL |
| 6376 | CPN-2402-MG1441 | 3 | 10000002 | 0 | 2024-02-14 21:18:58 | NULL | NULL | 0 | NULL | NULL | NULL |
| 6529 | CPN-2406-MG1594 | 3 | 10000002 | 0 | 2024-06-05 05:46:16 | NULL | NULL | 0 | NULL | NULL | NULL |
| 6692 | CPN-2403-MG1757 | 3 | 10000002 | 0 | 2024-03-01 06:19:39 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9408 | CPN-2507-BZQ014 | 1 | 10000002 | 0 | 2023-11-28 06:29:46 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9418 | CPN-2508-BVT859 | 2 | 10000002 | 0 | 2024-02-22 10:48:28 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9429 | CPN-2403-PB7T3X | 1 | 10000002 | 0 | 2024-03-06 10:17:38 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9430 | CPN-2404-HC9E5N | 1 | 10000002 | 0 | 2024-04-17 14:31:55 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9612 | CPN-2403-M7P9DK | 1 | 10000002 | 0 | 2024-03-12 17:21:35 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9614 | CPN-2312-R5V8CJ | 1 | 10000002 | 0 | 2023-12-12 20:30:00 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9615 | CPN-2506-ZK8D4W | 1 | 10000002 | 0 | 2025-06-30 16:33:21 | NULL | NULL | 0 | NULL | NULL | NULL |
| 9622 | CPN-2505-FG6Y2L | 1 | 10000002 | 0 | 2025-05-03 01:18:41 | NULL | NULL | 0 | NULL | NULL | NULL |

### dbo.EVoucher
用途：儲存會員電子禮券
總筆數（資料庫）：355

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| EVoucherID | int | NO |  | IDENTITY(1,1) |
| EVoucherCode | nvarchar(50) | NO |  |  |
| EVoucherTypeID | int | NO |  |  |
| UserID | int | NO |  |  |
| IsUsed | bit | NO |  |  |
| AcquiredTime | datetime2(7) | NO | sysutcdatetime() |  |
| UsedTime | datetime2(7) | YES | sysutcdatetime() |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_EVoucher (CLUSTERED) → EVoucherID
- **唯一性約束／索引**:
  - UQ_EVoucher_EVoucherCode (NONCLUSTERED) → EVoucherCode (UNIQUE CONSTRAINT)
- **其他索引**:
  - IX_EVoucher_user_used (NONCLUSTERED) → UserID, IsUsed, AcquiredTime
  - IX_EVoucher_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_EVoucher_EVoucherType: EVoucherTypeID → EVoucherTypeID | 參照 dbo.EVoucherType | ON UPDATE NO_ACTION / ON DELETE NO_ACTION
- FK_EVoucher_Users: UserID → User_ID | 參照 dbo.Users | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出條件：UserID ∈ {10000001, 10000002}
- 匯出筆數：4
- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。
| EVoucherID | EVoucherCode | EVoucherTypeID | UserID | IsUsed | AcquiredTime | UsedTime | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EV-FAMILY-MNPQ-064877 | 3 | 10000001 | 1 | 2024-10-29 15:17:44 | 2025-05-30 23:53:14 | 0 | NULL | NULL | NULL |
| 2 | EV-PIZZA-BCDF-969669 | 12 | 10000001 | 0 | 2025-01-14 07:58:55 | NULL | 0 | NULL | NULL | NULL |
| 3 | EV-STORE-BNXR-252844 | 4 | 10000001 | 0 | 2024-11-18 08:13:38 | NULL | 0 | NULL | NULL | NULL |
| 4 | EV-ICECREAM-GHJK-253496 | 15 | 10000002 | 1 | 2023-08-07 16:08:59 | 2023-11-24 09:25:43 | 0 | NULL | NULL | NULL |

### dbo.EVoucherToken
用途：儲存電子禮券的兌換 Token
總筆數（資料庫）：355

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| TokenID | int | NO |  | IDENTITY(1,1) |
| EVoucherID | int | NO |  |  |
| Token | varchar(64) | NO |  |  |
| ExpiresAt | datetime2(7) | NO |  |  |
| IsRevoked | bit | NO |  |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_EVoucherToken (CLUSTERED) → TokenID
- **唯一性約束／索引**:
  - UQ_EVoucherToken_Token (NONCLUSTERED) → Token (UNIQUE CONSTRAINT)
- **其他索引**:
  - IX_EVoucherToken_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_EVoucherToken_EVoucher: EVoucherID → EVoucherID | 參照 dbo.EVoucher | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出條件：EVoucher 所屬 UserID ∈ {10000001, 10000002}
- 匯出筆數：4
- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。
| TokenID | EVoucherID | Token | ExpiresAt | IsRevoked | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | TKN-GFWZIUGU-7603 | 2024-12-09 15:17:44 | 0 | 0 | NULL | NULL | NULL |
| 2 | 2 | TKN-0AFNJ3IW-7410 | 2025-04-08 07:58:55 | 0 | 0 | NULL | NULL | NULL |
| 3 | 3 | TKN-QBHYOJ30-9972 | 2025-08-05 09:01:17 | 0 | 0 | NULL | NULL | NULL |
| 4 | 4 | TKN-L62G3NV4-9235 | 2025-05-21 15:30:47 | 1 | 0 | NULL | NULL | NULL |

### dbo.EVoucherRedeemLog
用途：記錄電子禮券的核銷歷史
總筆數（資料庫）：794

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| RedeemID | int | NO |  | IDENTITY(1,1) |
| EVoucherID | int | NO |  |  |
| TokenID | int | YES |  |  |
| UserID | int | NO |  |  |
| ScannedAt | datetime2(7) | NO | sysutcdatetime() |  |
| Status | nvarchar(20) | NO |  |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_EVoucherRedeemLog (CLUSTERED) → RedeemID
- **其他索引**:
  - IX_EVoucherRedeemLog_voucher_user (NONCLUSTERED) → EVoucherID, UserID, ScannedAt
  - IX_EVoucherRedeemLog_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_EVoucherRedeemLog_EVoucher: EVoucherID → EVoucherID | 參照 dbo.EVoucher | ON UPDATE NO_ACTION / ON DELETE CASCADE
- FK_EVoucherRedeemLog_Token: TokenID → TokenID | 參照 dbo.EVoucherToken | ON UPDATE NO_ACTION / ON DELETE NO_ACTION
- FK_EVoucherRedeemLog_Users: UserID → User_ID | 參照 dbo.Users | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- CK_EVoucherRedeemLog_Status: (upper([Status])=N'REVOKED' OR upper([Status])=N'REJECTED' OR upper([Status])=N'EXPIRED' OR upper([Status])=N'ALREADYUSED' OR upper([Status])=N'APPROVED')

#### 種子資料
- 匯出條件：UserID ∈ {10000001, 10000002}
- 匯出筆數：5
- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。
| RedeemID | EVoucherID | TokenID | UserID | ScannedAt | Status | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 196 | 139 | 139 | 10000001 | 2025-07-17 08:55:01 | Revoked | 0 | NULL | NULL | NULL |
| 662 | 289 | 289 | 10000001 | 2023-05-10 22:43:48 | Revoked | 0 | NULL | NULL | NULL |
| 214 | 150 | 150 | 10000002 | 2024-06-04 16:17:29 | Approved | 0 | NULL | NULL | NULL |
| 242 | 168 | 168 | 10000002 | 2023-06-16 15:45:35 | Expired | 0 | NULL | NULL | NULL |
| 551 | 238 | 238 | 10000002 | 2024-08-21 09:12:36 | Revoked | 0 | NULL | NULL | NULL |

### dbo.MiniGame
用途：記錄遊戲進度和結果
總筆數（資料庫）：2000

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| PlayID | int | NO |  | IDENTITY(1,1) |
| UserID | int | NO |  |  |
| PetID | int | NO |  |  |
| Level | int | NO |  |  |
| MonsterCount | int | NO |  |  |
| SpeedMultiplier | decimal(5,2) | NO |  |  |
| Result | nvarchar(20) | NO |  |  |
| ExpGained | int | NO |  |  |
| ExpGainedTime | datetime2(7) | NO | sysutcdatetime() |  |
| PointsGained | int | NO |  |  |
| PointsGainedTime | datetime2(7) | NO | sysutcdatetime() |  |
| CouponGained | nvarchar(50) | NO |  |  |
| CouponGainedTime | datetime2(7) | NO | sysutcdatetime() |  |
| HungerDelta | int | NO |  |  |
| MoodDelta | int | NO |  |  |
| StaminaDelta | int | NO |  |  |
| CleanlinessDelta | int | NO |  |  |
| StartTime | datetime2(7) | NO | sysutcdatetime() |  |
| EndTime | datetime2(7) | YES | sysutcdatetime() |  |
| Aborted | bit | NO |  |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_MiniGame (CLUSTERED) → PlayID
- **其他索引**:
  - IX_MiniGame_user_time (NONCLUSTERED) → UserID, StartTime
  - IX_MiniGame_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_MiniGame_Pet: PetID → PetID | 參照 dbo.Pet | ON UPDATE NO_ACTION / ON DELETE NO_ACTION
- FK_MiniGame_Users: UserID → User_ID | 參照 dbo.Users | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出條件：UserID ∈ {10000001, 10000002}
- 匯出筆數：23
- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。
| PlayID | UserID | PetID | Level | MonsterCount | SpeedMultiplier | Result | ExpGained | ExpGainedTime | PointsGained | PointsGainedTime | CouponGained | CouponGainedTime | HungerDelta | MoodDelta | StaminaDelta | CleanlinessDelta | StartTime | EndTime | Aborted | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 2024-09-03 09:59:00 | 0 | 2024-09-03 09:59:00 | AUTO-SIGN-0000000000 | 2024-09-03 09:59:00 | -20 | -30 | -20 | -20 | 2024-09-03 09:36:58 | 2024-09-03 09:58:58 | 0 | 0 | NULL | NULL | NULL |
| 2 | 10000001 | 1 | 3 | 10 | 2.00 | Win | 300 | 2025-06-30 11:05:33 | 30 | 2025-06-30 11:05:33 | CPN-2506-WJ9F2T | 2025-06-30 11:05:33 | -20 | 30 | -20 | -20 | 2025-06-30 10:46:31 | 2025-06-30 11:05:31 | 0 | 0 | NULL | NULL | NULL |
| 3 | 10000001 | 1 | 1 | 6 | 1.00 | Win | 100 | 2023-07-01 13:49:37 | 10 | 2023-07-01 13:49:37 | AUTO-SIGN-0000000000 | 2023-07-01 13:49:37 | -20 | 30 | -20 | -20 | 2023-07-01 13:44:35 | 2023-07-01 13:49:35 | 0 | 0 | NULL | NULL | NULL |
| 4 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 2023-12-10 04:03:45 | 0 | 2023-12-10 04:03:45 | AUTO-SIGN-0000000000 | 2023-12-10 04:03:45 | -20 | -30 | -20 | -20 | 2023-12-10 03:41:43 | 2023-12-10 04:03:43 | 0 | 0 | NULL | NULL | NULL |
| 5 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 2025-06-23 00:02:37 | 0 | 2025-06-23 00:02:37 | AUTO-SIGN-0000000000 | 2025-06-23 00:02:37 | -20 | -30 | -20 | -20 | 2025-06-22 23:39:35 | 2025-06-23 00:02:35 | 0 | 0 | NULL | NULL | NULL |
| 6 | 10000001 | 1 | 2 | 8 | 1.50 | Win | 200 | 2023-09-03 19:10:11 | 20 | 2023-09-03 19:10:11 | AUTO-SIGN-0000000000 | 2023-09-03 19:10:11 | -20 | 30 | -20 | -20 | 2023-09-03 18:52:09 | 2023-09-03 19:10:09 | 0 | 0 | NULL | NULL | NULL |
| 7 | 10000001 | 1 | 3 | 10 | 2.00 | Abort | 0 | 2024-11-17 07:14:55 | 0 | 2024-11-17 07:14:55 | AUTO-SIGN-0000000000 | 2024-11-17 07:14:55 | -20 | 0 | -20 | -20 | 2024-11-17 07:08:53 | 2024-11-17 07:14:53 | 1 | 0 | NULL | NULL | NULL |
| 8 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 2025-05-07 19:57:09 | 0 | 2025-05-07 19:57:09 | AUTO-SIGN-0000000000 | 2025-05-07 19:57:09 | -20 | -30 | -20 | -20 | 2025-05-07 19:40:07 | 2025-05-07 19:57:07 | 0 | 0 | NULL | NULL | NULL |
| 9 | 10000001 | 1 | 3 | 10 | 2.00 | Win | 300 | 2024-03-08 10:07:56 | 30 | 2024-03-08 10:07:56 | CPN-2403-BQ8N4R | 2024-03-08 10:07:56 | -20 | 30 | -20 | -20 | 2024-03-08 09:49:54 | 2024-03-08 10:07:54 | 0 | 0 | NULL | NULL | NULL |
| 10 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 2024-05-15 08:34:28 | 0 | 2024-05-15 08:34:28 | AUTO-SIGN-0000000000 | 2024-05-15 08:34:28 | -20 | -30 | -20 | -20 | 2024-05-15 08:18:26 | 2024-05-15 08:34:26 | 0 | 0 | NULL | NULL | NULL |
| 11 | 10000001 | 1 | 3 | 10 | 2.00 | Win | 300 | 2023-12-01 20:41:09 | 30 | 2023-12-01 20:41:09 | CPN-2312-HG7K3M | 2023-12-01 20:41:09 | -20 | 30 | -20 | -20 | 2023-12-01 20:21:07 | 2023-12-01 20:41:07 | 0 | 0 | NULL | NULL | NULL |
| 12 | 10000002 | 2 | 3 | 10 | 2.00 | Win | 300 | 2024-03-12 17:21:35 | 30 | 2024-03-12 17:21:35 | CPN-2403-M7P9DK | 2024-03-12 17:21:35 | -20 | 30 | -20 | -20 | 2024-03-12 17:04:33 | 2024-03-12 17:21:33 | 0 | 0 | NULL | NULL | NULL |
| 13 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 2024-01-19 17:56:02 | 0 | 2024-01-19 17:56:02 | AUTO-SIGN-0000000000 | 2024-01-19 17:56:02 | -20 | -30 | -20 | -20 | 2024-01-19 17:39:00 | 2024-01-19 17:56:00 | 0 | 0 | NULL | NULL | NULL |
| 14 | 10000002 | 2 | 3 | 10 | 2.00 | Win | 300 | 2023-12-12 20:30:00 | 30 | 2023-12-12 20:30:00 | CPN-2312-R5V8CJ | 2023-12-12 20:30:00 | -20 | 30 | -20 | -20 | 2023-12-12 20:11:58 | 2023-12-12 20:29:58 | 0 | 0 | NULL | NULL | NULL |
| 15 | 10000002 | 2 | 3 | 10 | 2.00 | Win | 300 | 2025-06-30 16:33:21 | 30 | 2025-06-30 16:33:21 | CPN-2506-ZK8D4W | 2025-06-30 16:33:21 | -20 | 30 | -20 | -20 | 2025-06-30 16:12:19 | 2025-06-30 16:33:19 | 0 | 0 | NULL | NULL | NULL |
| 16 | 10000002 | 2 | 1 | 6 | 1.00 | Win | 100 | 2023-03-14 06:06:06 | 10 | 2023-03-14 06:06:06 | AUTO-SIGN-0000000000 | 2023-03-14 06:06:06 | -20 | 30 | -20 | -20 | 2023-03-14 06:01:04 | 2023-03-14 06:06:04 | 0 | 0 | NULL | NULL | NULL |
| 17 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 2025-07-26 07:16:15 | 0 | 2025-07-26 07:16:15 | AUTO-SIGN-0000000000 | 2025-07-26 07:16:15 | -20 | -30 | -20 | -20 | 2025-07-26 06:55:13 | 2025-07-26 07:16:13 | 0 | 0 | NULL | NULL | NULL |
| 18 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 2024-11-08 14:29:26 | 0 | 2024-11-08 14:29:26 | AUTO-SIGN-0000000000 | 2024-11-08 14:29:26 | -20 | -30 | -20 | -20 | 2024-11-08 14:08:24 | 2024-11-08 14:29:24 | 0 | 0 | NULL | NULL | NULL |
| 19 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 2023-08-06 13:08:58 | 0 | 2023-08-06 13:08:58 | AUTO-SIGN-0000000000 | 2023-08-06 13:08:58 | -20 | -30 | -20 | -20 | 2023-08-06 12:46:56 | 2023-08-06 13:08:56 | 0 | 0 | NULL | NULL | NULL |
| 20 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 2024-02-06 00:32:16 | 0 | 2024-02-06 00:32:16 | AUTO-SIGN-0000000000 | 2024-02-06 00:32:16 | -20 | -30 | -20 | -20 | 2024-02-06 00:13:14 | 2024-02-06 00:32:14 | 0 | 0 | NULL | NULL | NULL |
| 21 | 10000002 | 2 | 2 | 8 | 1.50 | Win | 200 | 2023-03-30 11:26:14 | 20 | 2023-03-30 11:26:14 | AUTO-SIGN-0000000000 | 2023-03-30 11:26:14 | -20 | 30 | -20 | -20 | 2023-03-30 11:16:12 | 2023-03-30 11:26:12 | 0 | 0 | NULL | NULL | NULL |
| 22 | 10000002 | 2 | 3 | 10 | 2.00 | Win | 300 | 2025-05-03 01:18:41 | 30 | 2025-05-03 01:18:41 | CPN-2505-FG6Y2L | 2025-05-03 01:18:41 | -20 | 30 | -20 | -20 | 2025-05-03 00:59:39 | 2025-05-03 01:18:39 | 0 | 0 | NULL | NULL | NULL |
| 23 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 2023-05-03 15:24:08 | 0 | 2023-05-03 15:24:08 | AUTO-SIGN-0000000000 | 2023-05-03 15:24:08 | -20 | -30 | -20 | -20 | 2023-05-03 15:04:06 | 2023-05-03 15:24:06 | 0 | 0 | NULL | NULL | NULL |

### dbo.Pet
用途：儲存會員的寵物資訊和狀態
總筆數（資料庫）：200

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| PetID | int | NO |  | IDENTITY(1,1) |
| UserID | int | NO |  |  |
| PetName | nvarchar(50) | NO |  |  |
| Level | int | NO |  |  |
| LevelUpTime | datetime2(7) | NO | sysutcdatetime() |  |
| Experience | int | NO |  |  |
| Hunger | int | NO |  |  |
| Mood | int | NO |  |  |
| Stamina | int | NO |  |  |
| Cleanliness | int | NO |  |  |
| Health | int | NO |  |  |
| SkinColor | varchar(10) | NO |  |  |
| SkinColorChangedTime | datetime2(7) | NO |  |  |
| BackgroundColor | nvarchar(20) | NO |  |  |
| BackgroundColorChangedTime | datetime2(7) | NO |  |  |
| PointsChanged_SkinColor | int | NO |  |  |
| PointsChanged_BackgroundColor | int | NO |  |  |
| PointsGained_LevelUp | int | NO |  |  |
| PointsGainedTime_LevelUp | datetime2(7) | NO | sysutcdatetime() |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |
| CurrentExperience | int | NO | 0 |  |
| ExperienceToNextLevel | int | YES |  |  |
| TotalPointsGained_LevelUp | int | YES | 0 |  |

#### 索引與鍵
- **主鍵**:
  - PK_Pet (CLUSTERED) → PetID
- **其他索引**:
  - IX_Pet_user (NONCLUSTERED) → UserID
  - IX_Pet_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_Pet_Users: UserID → User_ID | 參照 dbo.Users | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- CK_Pet_Cleanliness: ([Cleanliness]>=(0) AND [Cleanliness]<=(100))
- CK_Pet_Health: ([Health]>=(0) AND [Health]<=(100))
- CK_Pet_Hunger: ([Hunger]>=(0) AND [Hunger]<=(100))
- CK_Pet_Mood: ([Mood]>=(0) AND [Mood]<=(100))
- CK_Pet_Stamina: ([Stamina]>=(0) AND [Stamina]<=(100))

#### 種子資料
- 匯出條件：UserID ∈ {10000001, 10000002}
- 匯出筆數：2
- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。
| PetID | UserID | PetName | Level | LevelUpTime | Experience | Hunger | Mood | Stamina | Cleanliness | Health | SkinColor | SkinColorChangedTime | BackgroundColor | BackgroundColorChangedTime | PointsChanged_SkinColor | PointsChanged_BackgroundColor | PointsGained_LevelUp | PointsGainedTime_LevelUp | IsDeleted | DeletedAt | DeletedBy | DeleteReason | CurrentExperience | ExperienceToNextLevel | TotalPointsGained_LevelUp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 10000001 | 多多 | 4 | 2024-04-11 07:10:55 | 656 | 14 | 58 | 89 | 25 | 100 | #FFFF00 | 2023-02-22 09:10:06 | BG005 | 2025-04-09 17:03:40 | 2000 | 2500 | 10 | 2023-07-11 20:53:18 | 0 | NULL | NULL | NULL | 53 | 220 | 40 |
| 2 | 10000002 | 喵喵 | 38 | 2023-08-08 23:34:25 | 4019 | 55 | 15 | 57 | 14 | 94 | #800080 | 2024-12-11 04:53:18 | BG008 | 2024-08-25 17:19:48 | 3500 | 4000 | 40 | 2023-07-03 10:24:44 | 0 | NULL | NULL | NULL | 649 | 1535 | 920 |

### dbo.User_Wallet
用途：儲存會員當前點數餘額
總筆數（資料庫）：200

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| User_Id | int | NO |  |  |
| User_Point | int | NO | 0 |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_User_Wallet (CLUSTERED) → User_Id
- **其他索引**:
  - IX_User_Wallet_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_User_Wallet_Users: User_Id → User_ID | 參照 dbo.Users | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出條件：User_Id ∈ {10000001, 10000002}
- 匯出筆數：2
- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。
| User_Id | User_Point | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- |
| 10000001 | 60030 | 0 | NULL | NULL | NULL |
| 10000002 | 21666 | 0 | NULL | NULL | NULL |

### dbo.UserSignInStats
用途：記錄會員每日簽到日誌
總筆數（資料庫）：2470

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| LogID | int | NO |  | IDENTITY(1,1) |
| SignTime | datetime2(7) | NO | sysutcdatetime() |  |
| UserID | int | NO |  |  |
| PointsGained | int | NO |  |  |
| PointsGainedTime | datetime2(7) | NO | sysutcdatetime() |  |
| ExpGained | int | NO |  |  |
| ExpGainedTime | datetime2(7) | NO | sysutcdatetime() |  |
| CouponGained | nvarchar(50) | NO |  |  |
| CouponGainedTime | datetime2(7) | NO | sysutcdatetime() |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_UserSignInStats (CLUSTERED) → LogID
- **其他索引**:
  - IX_UserSignInStats_user_time (NONCLUSTERED) → UserID, SignTime
  - IX_UserSignInStats_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_UserSignInStats_Users: UserID → User_ID | 參照 dbo.Users | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出條件：UserID ∈ {10000001, 10000002}
- 匯出筆數：100
- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。
| LogID | SignTime | UserID | PointsGained | PointsGainedTime | ExpGained | ExpGainedTime | CouponGained | CouponGainedTime | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2401 | 2024-01-15 08:23:15 | 10000001 | 10 | 2024-01-15 08:23:15 | 5 | 2024-01-15 08:23:15 | AUTO-SIGN-0000000000 | 2024-01-15 08:23:15 | 0 | NULL | NULL | NULL |
| 2402 | 2024-01-16 08:45:22 | 10000001 | 10 | 2024-01-16 08:45:22 | 5 | 2024-01-16 08:45:22 | AUTO-SIGN-0000000000 | 2024-01-16 08:45:22 | 0 | NULL | NULL | NULL |
| 2403 | 2024-01-17 08:17:38 | 10000001 | 15 | 2024-01-17 08:17:38 | 8 | 2024-01-17 08:17:38 | AUTO-SIGN-0000000000 | 2024-01-17 08:17:38 | 0 | NULL | NULL | NULL |
| 2404 | 2024-01-18 08:52:41 | 10000001 | 15 | 2024-01-18 08:52:41 | 8 | 2024-01-18 08:52:41 | AUTO-SIGN-0000000000 | 2024-01-18 08:52:41 | 0 | NULL | NULL | NULL |
| 2405 | 2024-01-19 08:34:12 | 10000001 | 20 | 2024-01-19 08:34:12 | 10 | 2024-01-19 08:34:12 | AUTO-SIGN-0000000000 | 2024-01-19 08:34:12 | 0 | NULL | NULL | NULL |
| 2406 | 2024-01-20 09:28:55 | 10000001 | 20 | 2024-01-20 09:28:55 | 10 | 2024-01-20 09:28:55 | AUTO-SIGN-0000000000 | 2024-01-20 09:28:55 | 0 | NULL | NULL | NULL |
| 2407 | 2024-01-21 09:45:18 | 10000001 | 30 | 2024-01-21 09:45:18 | 15 | 2024-01-21 09:45:18 | CPN-2401-A7B2K9 | 2024-01-21 09:45:18 | 0 | NULL | NULL | NULL |
| 2408 | 2024-01-22 08:19:47 | 10000001 | 20 | 2024-01-22 08:19:47 | 0 | 2024-01-22 08:19:47 | AUTO-SIGN-0000000000 | 2024-01-22 08:19:47 | 0 | NULL | NULL | NULL |
| 2409 | 2024-01-23 08:41:23 | 10000001 | 20 | 2024-01-23 08:41:23 | 0 | 2024-01-23 08:41:23 | AUTO-SIGN-0000000000 | 2024-01-23 08:41:23 | 0 | NULL | NULL | NULL |
| 2410 | 2024-01-24 21:15:32 | 10000001 | 20 | 2024-01-24 21:15:32 | 0 | 2024-01-24 21:15:32 | AUTO-SIGN-0000000000 | 2024-01-24 21:15:32 | 0 | NULL | NULL | NULL |
| 2411 | 2024-01-26 08:52:14 | 10000001 | 10 | 2024-01-26 08:52:14 | 5 | 2024-01-26 08:52:14 | AUTO-SIGN-0000000000 | 2024-01-26 08:52:14 | 0 | NULL | NULL | NULL |
| 2412 | 2024-01-27 09:18:36 | 10000001 | 10 | 2024-01-27 09:18:36 | 5 | 2024-01-27 09:18:36 | AUTO-SIGN-0000000000 | 2024-01-27 09:18:36 | 0 | NULL | NULL | NULL |
| 2413 | 2024-01-28 09:52:41 | 10000001 | 15 | 2024-01-28 09:52:41 | 8 | 2024-01-28 09:52:41 | AUTO-SIGN-0000000000 | 2024-01-28 09:52:41 | 0 | NULL | NULL | NULL |
| 2414 | 2024-01-29 08:27:19 | 10000001 | 15 | 2024-01-29 08:27:19 | 8 | 2024-01-29 08:27:19 | AUTO-SIGN-0000000000 | 2024-01-29 08:27:19 | 0 | NULL | NULL | NULL |
| 2415 | 2024-01-30 08:38:52 | 10000001 | 20 | 2024-01-30 08:38:52 | 10 | 2024-01-30 08:38:52 | AUTO-SIGN-0000000000 | 2024-01-30 08:38:52 | 0 | NULL | NULL | NULL |
| 2416 | 2024-01-31 08:15:47 | 10000001 | 20 | 2024-01-31 08:15:47 | 10 | 2024-01-31 08:15:47 | AUTO-SIGN-0000000000 | 2024-01-31 08:15:47 | 0 | NULL | NULL | NULL |
| 2417 | 2024-02-01 08:44:28 | 10000001 | 30 | 2024-02-01 08:44:28 | 15 | 2024-02-01 08:44:28 | CPN-2402-XW4H8P | 2024-02-01 08:44:28 | 0 | NULL | NULL | NULL |
| 2418 | 2024-02-02 08:23:55 | 10000001 | 20 | 2024-02-02 08:23:55 | 0 | 2024-02-02 08:23:55 | AUTO-SIGN-0000000000 | 2024-02-02 08:23:55 | 0 | NULL | NULL | NULL |
| 2419 | 2024-02-03 09:37:12 | 10000001 | 30 | 2024-02-03 09:37:12 | 200 | 2024-02-03 09:37:12 | AUTO-SIGN-0000000000 | 2024-02-03 09:37:12 | 0 | NULL | NULL | NULL |
| 2420 | 2024-02-04 10:05:48 | 10000001 | 30 | 2024-02-04 10:05:48 | 200 | 2024-02-04 10:05:48 | AUTO-SIGN-0000000000 | 2024-02-04 10:05:48 | 0 | NULL | NULL | NULL |
| 2421 | 2024-02-05 08:19:33 | 10000001 | 20 | 2024-02-05 08:19:33 | 0 | 2024-02-05 08:19:33 | AUTO-SIGN-0000000000 | 2024-02-05 08:19:33 | 0 | NULL | NULL | NULL |
| 2422 | 2024-02-06 08:47:21 | 10000001 | 20 | 2024-02-06 08:47:21 | 0 | 2024-02-06 08:47:21 | AUTO-SIGN-0000000000 | 2024-02-06 08:47:21 | 0 | NULL | NULL | NULL |
| 2423 | 2024-02-07 20:42:18 | 10000001 | 20 | 2024-02-07 20:42:18 | 0 | 2024-02-07 20:42:18 | AUTO-SIGN-0000000000 | 2024-02-07 20:42:18 | 0 | NULL | NULL | NULL |
| 2424 | 2024-02-08 08:31:45 | 10000001 | 50 | 2024-02-08 08:31:45 | 25 | 2024-02-08 08:31:45 | CPN-2402-M9N5QT | 2024-02-08 08:31:45 | 0 | NULL | NULL | NULL |
| 2425 | 2024-02-09 08:56:12 | 10000001 | 20 | 2024-02-09 08:56:12 | 0 | 2024-02-09 08:56:12 | AUTO-SIGN-0000000000 | 2024-02-09 08:56:12 | 0 | NULL | NULL | NULL |
| 2426 | 2024-02-10 09:22:37 | 10000001 | 30 | 2024-02-10 09:22:37 | 200 | 2024-02-10 09:22:37 | AUTO-SIGN-0000000000 | 2024-02-10 09:22:37 | 0 | NULL | NULL | NULL |
| 2427 | 2024-02-11 09:48:53 | 10000001 | 30 | 2024-02-11 09:48:53 | 200 | 2024-02-11 09:48:53 | AUTO-SIGN-0000000000 | 2024-02-11 09:48:53 | 0 | NULL | NULL | NULL |
| 2428 | 2024-02-13 08:14:26 | 10000001 | 10 | 2024-02-13 08:14:26 | 5 | 2024-02-13 08:14:26 | AUTO-SIGN-0000000000 | 2024-02-13 08:14:26 | 0 | NULL | NULL | NULL |
| 2429 | 2024-02-14 08:38:41 | 10000001 | 10 | 2024-02-14 08:38:41 | 5 | 2024-02-14 08:38:41 | AUTO-SIGN-0000000000 | 2024-02-14 08:38:41 | 0 | NULL | NULL | NULL |
| 2430 | 2024-02-15 08:25:19 | 10000001 | 15 | 2024-02-15 08:25:19 | 8 | 2024-02-15 08:25:19 | AUTO-SIGN-0000000000 | 2024-02-15 08:25:19 | 0 | NULL | NULL | NULL |
| 2431 | 2024-02-16 08:49:52 | 10000001 | 15 | 2024-02-16 08:49:52 | 8 | 2024-02-16 08:49:52 | AUTO-SIGN-0000000000 | 2024-02-16 08:49:52 | 0 | NULL | NULL | NULL |
| 2432 | 2024-02-17 09:31:24 | 10000001 | 20 | 2024-02-17 09:31:24 | 10 | 2024-02-17 09:31:24 | AUTO-SIGN-0000000000 | 2024-02-17 09:31:24 | 0 | NULL | NULL | NULL |
| 2433 | 2024-02-18 10:14:37 | 10000001 | 20 | 2024-02-18 10:14:37 | 10 | 2024-02-18 10:14:37 | AUTO-SIGN-0000000000 | 2024-02-18 10:14:37 | 0 | NULL | NULL | NULL |
| 2434 | 2024-02-19 08:22:48 | 10000001 | 30 | 2024-02-19 08:22:48 | 15 | 2024-02-19 08:22:48 | CPN-2402-R3V7CJ | 2024-02-19 08:22:48 | 0 | NULL | NULL | NULL |
| 2435 | 2024-02-20 08:46:15 | 10000001 | 20 | 2024-02-20 08:46:15 | 0 | 2024-02-20 08:46:15 | AUTO-SIGN-0000000000 | 2024-02-20 08:46:15 | 0 | NULL | NULL | NULL |
| 2436 | 2024-02-21 08:18:33 | 10000001 | 20 | 2024-02-21 08:18:33 | 0 | 2024-02-21 08:18:33 | AUTO-SIGN-0000000000 | 2024-02-21 08:18:33 | 0 | NULL | NULL | NULL |
| 2437 | 2024-02-22 08:53:27 | 10000001 | 20 | 2024-02-22 08:53:27 | 0 | 2024-02-22 08:53:27 | AUTO-SIGN-0000000000 | 2024-02-22 08:53:27 | 0 | NULL | NULL | NULL |
| 2438 | 2024-02-23 08:31:56 | 10000001 | 20 | 2024-02-23 08:31:56 | 0 | 2024-02-23 08:31:56 | AUTO-SIGN-0000000000 | 2024-02-23 08:31:56 | 0 | NULL | NULL | NULL |
| 2439 | 2024-02-24 09:25:42 | 10000001 | 30 | 2024-02-24 09:25:42 | 200 | 2024-02-24 09:25:42 | AUTO-SIGN-0000000000 | 2024-02-24 09:25:42 | 0 | NULL | NULL | NULL |
| 2440 | 2024-02-25 09:58:18 | 10000001 | 30 | 2024-02-25 09:58:18 | 200 | 2024-02-25 09:58:18 | AUTO-SIGN-0000000000 | 2024-02-25 09:58:18 | 0 | NULL | NULL | NULL |
| 2441 | 2024-02-26 08:17:45 | 10000001 | 50 | 2024-02-26 08:17:45 | 25 | 2024-02-26 08:17:45 | CPN-2402-FG6Y2L | 2024-02-26 08:17:45 | 0 | NULL | NULL | NULL |
| 2442 | 2024-02-27 08:42:33 | 10000001 | 20 | 2024-02-27 08:42:33 | 0 | 2024-02-27 08:42:33 | AUTO-SIGN-0000000000 | 2024-02-27 08:42:33 | 0 | NULL | NULL | NULL |
| 2443 | 2024-02-28 08:28:19 | 10000001 | 20 | 2024-02-28 08:28:19 | 0 | 2024-02-28 08:28:19 | AUTO-SIGN-0000000000 | 2024-02-28 08:28:19 | 0 | NULL | NULL | NULL |
| 2444 | 2024-02-29 21:18:47 | 10000001 | 20 | 2024-02-29 21:18:47 | 0 | 2024-02-29 21:18:47 | AUTO-SIGN-0000000000 | 2024-02-29 21:18:47 | 0 | NULL | NULL | NULL |
| 2445 | 2024-03-01 08:35:52 | 10000001 | 20 | 2024-03-01 08:35:52 | 0 | 2024-03-01 08:35:52 | AUTO-SIGN-0000000000 | 2024-03-01 08:35:52 | 0 | NULL | NULL | NULL |
| 2446 | 2024-03-02 09:41:28 | 10000001 | 30 | 2024-03-02 09:41:28 | 200 | 2024-03-02 09:41:28 | AUTO-SIGN-0000000000 | 2024-03-02 09:41:28 | 0 | NULL | NULL | NULL |
| 2447 | 2024-03-03 10:07:15 | 10000001 | 30 | 2024-03-03 10:07:15 | 200 | 2024-03-03 10:07:15 | AUTO-SIGN-0000000000 | 2024-03-03 10:07:15 | 0 | NULL | NULL | NULL |
| 2448 | 2024-03-04 08:24:37 | 10000001 | 80 | 2024-03-04 08:24:37 | 40 | 2024-03-04 08:24:37 | CPN-2403-ZK8D4W | 2024-03-04 08:24:37 | 0 | NULL | NULL | NULL |
| 2449 | 2024-03-05 08:51:23 | 10000001 | 20 | 2024-03-05 08:51:23 | 0 | 2024-03-05 08:51:23 | AUTO-SIGN-0000000000 | 2024-03-05 08:51:23 | 0 | NULL | NULL | NULL |
| 2450 | 2024-03-06 08:16:48 | 10000001 | 20 | 2024-03-06 08:16:48 | 0 | 2024-03-06 08:16:48 | AUTO-SIGN-0000000000 | 2024-03-06 08:16:48 | 0 | NULL | NULL | NULL |
| 2451 | 2024-01-20 14:32:18 | 10000002 | 10 | 2024-01-20 14:32:18 | 5 | 2024-01-20 14:32:18 | AUTO-SIGN-0000000000 | 2024-01-20 14:32:18 | 0 | NULL | NULL | NULL |
| 2452 | 2024-01-21 22:15:47 | 10000002 | 10 | 2024-01-21 22:15:47 | 5 | 2024-01-21 22:15:47 | AUTO-SIGN-0000000000 | 2024-01-21 22:15:47 | 0 | NULL | NULL | NULL |
| 2453 | 2024-01-22 09:18:33 | 10000002 | 15 | 2024-01-22 09:18:33 | 8 | 2024-01-22 09:18:33 | AUTO-SIGN-0000000000 | 2024-01-22 09:18:33 | 0 | NULL | NULL | NULL |
| 2454 | 2024-01-26 19:47:22 | 10000002 | 20 | 2024-01-26 19:47:22 | 0 | 2024-01-26 19:47:22 | AUTO-SIGN-0000000000 | 2024-01-26 19:47:22 | 0 | NULL | NULL | NULL |
| 2455 | 2024-01-27 11:23:45 | 10000002 | 10 | 2024-01-27 11:23:45 | 5 | 2024-01-27 11:23:45 | AUTO-SIGN-0000000000 | 2024-01-27 11:23:45 | 0 | NULL | NULL | NULL |
| 2456 | 2024-01-28 20:09:14 | 10000002 | 15 | 2024-01-28 20:09:14 | 8 | 2024-01-28 20:09:14 | AUTO-SIGN-0000000000 | 2024-01-28 20:09:14 | 0 | NULL | NULL | NULL |
| 2457 | 2024-02-01 08:42:17 | 10000002 | 20 | 2024-02-01 08:42:17 | 0 | 2024-02-01 08:42:17 | AUTO-SIGN-0000000000 | 2024-02-01 08:42:17 | 0 | NULL | NULL | NULL |
| 2458 | 2024-02-02 16:55:38 | 10000002 | 10 | 2024-02-02 16:55:38 | 5 | 2024-02-02 16:55:38 | AUTO-SIGN-0000000000 | 2024-02-02 16:55:38 | 0 | NULL | NULL | NULL |
| 2459 | 2024-02-03 13:27:51 | 10000002 | 15 | 2024-02-03 13:27:51 | 8 | 2024-02-03 13:27:51 | AUTO-SIGN-0000000000 | 2024-02-03 13:27:51 | 0 | NULL | NULL | NULL |
| 2460 | 2024-02-04 21:14:29 | 10000002 | 15 | 2024-02-04 21:14:29 | 8 | 2024-02-04 21:14:29 | AUTO-SIGN-0000000000 | 2024-02-04 21:14:29 | 0 | NULL | NULL | NULL |
| 2461 | 2024-02-08 10:38:42 | 10000002 | 20 | 2024-02-08 10:38:42 | 0 | 2024-02-08 10:38:42 | AUTO-SIGN-0000000000 | 2024-02-08 10:38:42 | 0 | NULL | NULL | NULL |
| 2462 | 2024-02-09 18:22:15 | 10000002 | 10 | 2024-02-09 18:22:15 | 5 | 2024-02-09 18:22:15 | AUTO-SIGN-0000000000 | 2024-02-09 18:22:15 | 0 | NULL | NULL | NULL |
| 2463 | 2024-02-14 07:45:33 | 10000002 | 20 | 2024-02-14 07:45:33 | 0 | 2024-02-14 07:45:33 | AUTO-SIGN-0000000000 | 2024-02-14 07:45:33 | 0 | NULL | NULL | NULL |
| 2464 | 2024-02-15 15:11:47 | 10000002 | 10 | 2024-02-15 15:11:47 | 5 | 2024-02-15 15:11:47 | AUTO-SIGN-0000000000 | 2024-02-15 15:11:47 | 0 | NULL | NULL | NULL |
| 2465 | 2024-02-16 12:58:21 | 10000002 | 15 | 2024-02-16 12:58:21 | 8 | 2024-02-16 12:58:21 | AUTO-SIGN-0000000000 | 2024-02-16 12:58:21 | 0 | NULL | NULL | NULL |
| 2466 | 2024-02-17 19:33:54 | 10000002 | 15 | 2024-02-17 19:33:54 | 8 | 2024-02-17 19:33:54 | AUTO-SIGN-0000000000 | 2024-02-17 19:33:54 | 0 | NULL | NULL | NULL |
| 2467 | 2024-02-18 22:07:18 | 10000002 | 20 | 2024-02-18 22:07:18 | 10 | 2024-02-18 22:07:18 | AUTO-SIGN-0000000000 | 2024-02-18 22:07:18 | 0 | NULL | NULL | NULL |
| 2468 | 2024-02-22 09:25:46 | 10000002 | 20 | 2024-02-22 09:25:46 | 0 | 2024-02-22 09:25:46 | AUTO-SIGN-0000000000 | 2024-02-22 09:25:46 | 0 | NULL | NULL | NULL |
| 2469 | 2024-02-23 17:41:32 | 10000002 | 10 | 2024-02-23 17:41:32 | 5 | 2024-02-23 17:41:32 | AUTO-SIGN-0000000000 | 2024-02-23 17:41:32 | 0 | NULL | NULL | NULL |
| 2470 | 2024-02-24 14:19:08 | 10000002 | 15 | 2024-02-24 14:19:08 | 8 | 2024-02-24 14:19:08 | AUTO-SIGN-0000000000 | 2024-02-24 14:19:08 | 0 | NULL | NULL | NULL |
| 2471 | 2024-02-29 11:47:25 | 10000002 | 20 | 2024-02-29 11:47:25 | 0 | 2024-02-29 11:47:25 | AUTO-SIGN-0000000000 | 2024-02-29 11:47:25 | 0 | NULL | NULL | NULL |
| 2472 | 2024-03-01 20:33:17 | 10000002 | 10 | 2024-03-01 20:33:17 | 5 | 2024-03-01 20:33:17 | AUTO-SIGN-0000000000 | 2024-03-01 20:33:17 | 0 | NULL | NULL | NULL |
| 2473 | 2024-03-02 08:52:41 | 10000002 | 15 | 2024-03-02 08:52:41 | 8 | 2024-03-02 08:52:41 | AUTO-SIGN-0000000000 | 2024-03-02 08:52:41 | 0 | NULL | NULL | NULL |
| 2474 | 2024-03-03 16:08:29 | 10000002 | 15 | 2024-03-03 16:08:29 | 8 | 2024-03-03 16:08:29 | AUTO-SIGN-0000000000 | 2024-03-03 16:08:29 | 0 | NULL | NULL | NULL |
| 2475 | 2024-03-04 13:44:55 | 10000002 | 20 | 2024-03-04 13:44:55 | 10 | 2024-03-04 13:44:55 | AUTO-SIGN-0000000000 | 2024-03-04 13:44:55 | 0 | NULL | NULL | NULL |
| 2476 | 2024-03-05 21:29:13 | 10000002 | 20 | 2024-03-05 21:29:13 | 10 | 2024-03-05 21:29:13 | AUTO-SIGN-0000000000 | 2024-03-05 21:29:13 | 0 | NULL | NULL | NULL |
| 2477 | 2024-03-06 10:17:38 | 10000002 | 30 | 2024-03-06 10:17:38 | 15 | 2024-03-06 10:17:38 | CPN-2403-PB7T3X | 2024-03-06 10:17:38 | 0 | NULL | NULL | NULL |
| 2478 | 2024-03-11 18:55:24 | 10000002 | 20 | 2024-03-11 18:55:24 | 0 | 2024-03-11 18:55:24 | AUTO-SIGN-0000000000 | 2024-03-11 18:55:24 | 0 | NULL | NULL | NULL |
| 2479 | 2024-03-12 07:31:47 | 10000002 | 10 | 2024-03-12 07:31:47 | 5 | 2024-03-12 07:31:47 | AUTO-SIGN-0000000000 | 2024-03-12 07:31:47 | 0 | NULL | NULL | NULL |
| 2480 | 2024-03-13 15:23:19 | 10000002 | 15 | 2024-03-13 15:23:19 | 8 | 2024-03-13 15:23:19 | AUTO-SIGN-0000000000 | 2024-03-13 15:23:19 | 0 | NULL | NULL | NULL |
| 2481 | 2024-03-19 12:09:52 | 10000002 | 20 | 2024-03-19 12:09:52 | 0 | 2024-03-19 12:09:52 | AUTO-SIGN-0000000000 | 2024-03-19 12:09:52 | 0 | NULL | NULL | NULL |
| 2482 | 2024-03-20 19:46:37 | 10000002 | 10 | 2024-03-20 19:46:37 | 5 | 2024-03-20 19:46:37 | AUTO-SIGN-0000000000 | 2024-03-20 19:46:37 | 0 | NULL | NULL | NULL |
| 2483 | 2024-03-21 09:14:21 | 10000002 | 15 | 2024-03-21 09:14:21 | 8 | 2024-03-21 09:14:21 | AUTO-SIGN-0000000000 | 2024-03-21 09:14:21 | 0 | NULL | NULL | NULL |
| 2484 | 2024-03-22 22:38:45 | 10000002 | 15 | 2024-03-22 22:38:45 | 8 | 2024-03-22 22:38:45 | AUTO-SIGN-0000000000 | 2024-03-22 22:38:45 | 0 | NULL | NULL | NULL |
| 2485 | 2024-03-27 14:52:33 | 10000002 | 20 | 2024-03-27 14:52:33 | 0 | 2024-03-27 14:52:33 | AUTO-SIGN-0000000000 | 2024-03-27 14:52:33 | 0 | NULL | NULL | NULL |
| 2486 | 2024-03-28 08:27:16 | 10000002 | 10 | 2024-03-28 08:27:16 | 5 | 2024-03-28 08:27:16 | AUTO-SIGN-0000000000 | 2024-03-28 08:27:16 | 0 | NULL | NULL | NULL |
| 2487 | 2024-04-02 17:15:48 | 10000002 | 20 | 2024-04-02 17:15:48 | 0 | 2024-04-02 17:15:48 | AUTO-SIGN-0000000000 | 2024-04-02 17:15:48 | 0 | NULL | NULL | NULL |
| 2488 | 2024-04-03 11:43:29 | 10000002 | 10 | 2024-04-03 11:43:29 | 5 | 2024-04-03 11:43:29 | AUTO-SIGN-0000000000 | 2024-04-03 11:43:29 | 0 | NULL | NULL | NULL |
| 2489 | 2024-04-04 20:21:14 | 10000002 | 15 | 2024-04-04 20:21:14 | 8 | 2024-04-04 20:21:14 | AUTO-SIGN-0000000000 | 2024-04-04 20:21:14 | 0 | NULL | NULL | NULL |
| 2490 | 2024-04-05 13:58:37 | 10000002 | 15 | 2024-04-05 13:58:37 | 8 | 2024-04-05 13:58:37 | AUTO-SIGN-0000000000 | 2024-04-05 13:58:37 | 0 | NULL | NULL | NULL |
| 2491 | 2024-04-11 09:36:52 | 10000002 | 20 | 2024-04-11 09:36:52 | 0 | 2024-04-11 09:36:52 | AUTO-SIGN-0000000000 | 2024-04-11 09:36:52 | 0 | NULL | NULL | NULL |
| 2492 | 2024-04-12 16:14:28 | 10000002 | 10 | 2024-04-12 16:14:28 | 5 | 2024-04-12 16:14:28 | AUTO-SIGN-0000000000 | 2024-04-12 16:14:28 | 0 | NULL | NULL | NULL |
| 2493 | 2024-04-13 21:47:19 | 10000002 | 15 | 2024-04-13 21:47:19 | 8 | 2024-04-13 21:47:19 | AUTO-SIGN-0000000000 | 2024-04-13 21:47:19 | 0 | NULL | NULL | NULL |
| 2494 | 2024-04-14 10:25:41 | 10000002 | 15 | 2024-04-14 10:25:41 | 8 | 2024-04-14 10:25:41 | AUTO-SIGN-0000000000 | 2024-04-14 10:25:41 | 0 | NULL | NULL | NULL |
| 2495 | 2024-04-15 18:09:23 | 10000002 | 20 | 2024-04-15 18:09:23 | 10 | 2024-04-15 18:09:23 | AUTO-SIGN-0000000000 | 2024-04-15 18:09:23 | 0 | NULL | NULL | NULL |
| 2496 | 2024-04-16 07:53:38 | 10000002 | 20 | 2024-04-16 07:53:38 | 10 | 2024-04-16 07:53:38 | AUTO-SIGN-0000000000 | 2024-04-16 07:53:38 | 0 | NULL | NULL | NULL |
| 2497 | 2024-04-17 14:31:55 | 10000002 | 30 | 2024-04-17 14:31:55 | 15 | 2024-04-17 14:31:55 | CPN-2404-HC9E5N | 2024-04-17 14:31:55 | 0 | NULL | NULL | NULL |
| 2498 | 2024-04-18 22:18:47 | 10000002 | 20 | 2024-04-18 22:18:47 | 0 | 2024-04-18 22:18:47 | AUTO-SIGN-0000000000 | 2024-04-18 22:18:47 | 0 | NULL | NULL | NULL |
| 2499 | 2024-04-19 11:42:13 | 10000002 | 20 | 2024-04-19 11:42:13 | 0 | 2024-04-19 11:42:13 | AUTO-SIGN-0000000000 | 2024-04-19 11:42:13 | 0 | NULL | NULL | NULL |
| 2500 | 2024-04-24 15:27:39 | 10000002 | 20 | 2024-04-24 15:27:39 | 0 | 2024-04-24 15:27:39 | AUTO-SIGN-0000000000 | 2024-04-24 15:27:39 | 0 | NULL | NULL | NULL |

### dbo.WalletHistory
用途：記錄會員點數變動歷史
總筆數（資料庫）：1923

#### 欄位結構
| Column | Data Type | Nullable | Default | Extra |
| --- | --- | --- | --- | --- |
| LogID | int | NO |  | IDENTITY(1,1) |
| UserID | int | NO |  |  |
| ChangeType | nvarchar(20) | NO |  |  |
| PointsChanged | int | NO |  |  |
| ItemCode | nvarchar(50) | YES |  |  |
| Description | nvarchar(255) | YES |  |  |
| ChangeTime | datetime2(7) | NO | sysutcdatetime() |  |
| IsDeleted | bit | NO | 0 |  |
| DeletedAt | datetime2(7) | YES |  |  |
| DeletedBy | int | YES |  |  |
| DeleteReason | nvarchar(500) | YES |  |  |

#### 索引與鍵
- **主鍵**:
  - PK_WalletHistory (CLUSTERED) → LogID
- **其他索引**:
  - IX_WalletHistory_user_time (NONCLUSTERED) → UserID, ChangeTime
  - IX_WalletHistory_type_time (NONCLUSTERED) → ChangeType, ChangeTime
  - IX_WalletHistory_IsDeleted (NONCLUSTERED) → IsDeleted | Filter: ([IsDeleted]=(0))

#### 外鍵
- FK_WalletHistory_Users: UserID → User_ID | 參照 dbo.Users | ON UPDATE NO_ACTION / ON DELETE NO_ACTION

#### CHECK 約束
- 無 CHECK 約束

#### 種子資料
- 匯出條件：UserID ∈ {10000001, 10000002}
- 匯出筆數：10
- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。
| LogID | UserID | ChangeType | PointsChanged | ItemCode | Description | ChangeTime | IsDeleted | DeletedAt | DeletedBy | DeleteReason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 10000001 | Point | -30000 | EV-FAMILY-MNPQ-064877 | 會員點數兌換電子禮券 | 2024-10-29 15:17:44 | 0 | NULL | NULL | NULL |
| 7 | 10000001 | Point | 30 | NULL | 小遊戲勝利獲得會員點數 | 2023-12-08 03:34:50 | 0 | NULL | NULL | NULL |
| 1929 | 10000001 | Point | -2000 | #FFFF00 | 購買寵物皮膚顏色 | 2023-02-22 09:10:06 | 0 | NULL | NULL | NULL |
| 1930 | 10000001 | Point | -2500 | BG005 | 購買寵物背景 | 2025-04-09 17:03:40 | 0 | NULL | NULL | NULL |
| 1939 | 10000001 | Point | 94500 | INIT-BAL-001 | Initial account balance - retroactive logging | 2023-02-22 08:00:00 | 0 | NULL | NULL | NULL |
| 8 | 10000002 | Point | 446 | NULL | 活動送會員點數 | 2025-09-16 18:34:01.438976 | 0 | NULL | NULL | NULL |
| 11 | 10000002 | Point | -40000 | EV-ICECREAM-GHJK-253496 | 會員點數兌換電子禮券 | 2023-08-07 16:08:59 | 0 | NULL | NULL | NULL |
| 1931 | 10000002 | Point | -3500 | #800080 | 購買寵物皮膚顏色 | 2024-12-11 04:53:18 | 0 | NULL | NULL | NULL |
| 1932 | 10000002 | Point | -4000 | BG008 | 購買寵物背景 | 2024-08-25 17:19:48 | 0 | NULL | NULL | NULL |
| 1940 | 10000002 | Point | 68720 | INIT-BAL-002 | Initial account balance - retroactive logging | 2023-08-07 15:00:00 | 0 | NULL | NULL | NULL |
