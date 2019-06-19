import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/8DE8C06C-7B02-A94C-83C7-0B69A0DC11B2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/DDE6FE04-5BE3-0E41-AFAD-352070A12875.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/422C374A-78FF-7646-ABFB-CC247D64AA86.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/615EB4CA-C299-5D44-8C36-DD3C3A6A7947.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/19BF3914-508B-3042-8F23-A8E5C27A8BD2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/98E4C77D-6FA1-E841-A922-23243CAA41F5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/D9E0463F-1191-1C45-99AA-F8E3F6C11BD5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/439537FC-F172-3B41-9536-9B87BEC248EC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/71042589-71C0-A949-AAC0-2E1F0B07A968.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/D36D3DBC-D0A7-FB4D-87F5-C0C36F595C22.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/5A00978E-086D-2E4C-9D58-B7225F91327A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/C2E50B27-ADF3-5544-905A-60DF6680F63B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/58247A7F-31C1-FA44-8366-EB94AA90D833.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/368ADABE-2387-684E-BB64-F6B996C485E8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/8C445687-FFFA-4248-97A3-D61EE500BE1C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/4293DAFD-93A0-564C-857C-AC2C710A8F65.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/0A135691-E322-AC4B-A7B2-3CD4E43102D2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/0F0DD7D7-E535-8F4E-8710-6A5966FD3DD6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/2A8C2678-D605-C044-907C-FF10069F3FF4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/4AA667E0-09F5-B24E-9D87-227241B50972.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/B383BF8F-7DF6-4541-A57F-9C8C54C71287.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/D80EE4EF-DA75-4B43-A187-42C8DE818C54.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/E4D73CC8-7AEA-FC4A-8C09-AFF08C1C7AC9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2D18F1E6-8428-D649-A987-4F80F275ECBE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/DAAC15AD-6E4B-B54C-A918-407B7CE00211.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/9A090A0D-A5E5-8C42-9631-347F405FC632.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/AC443A13-B900-684E-911A-6E278635A4B4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/7D0371D6-85BA-6C4D-BB7D-4FB4FDA88036.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/6C281706-EA8C-3948-98EE-D2B8C637138B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/137C87DE-8594-1F45-B4F9-D5949A22446E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/181901BE-CB87-C946-BA99-41A9137C5570.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/80D555F5-D1E3-D048-98E2-507A2E2280C5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/1B0DC179-4B97-8046-9DDD-BB8FC3CF9CCE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/062B1E29-9D6A-1047-97C2-17F7D74D97E0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/18E609CF-BE1F-CD49-8C7C-DA1E56901FE5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/485C4663-DF6A-E34F-8448-F9ACACBC7AF9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/343D3029-5983-504C-B91C-09C763840103.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/4A4CA5CE-AA6A-DD46-B11C-9F26E5213F87.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/878F0073-6B50-404E-9BC3-47C2D16A2C1D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/3D00B4A4-E8E9-BA49-80EA-D01D7564260C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/0B422226-6B24-DD4D-B036-B2F5E3AB5686.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/933EAFEA-2C93-154C-BD7A-A5530B5B59DD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/9CFAC342-E6F5-DA40-BD96-78F8F8C20874.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/58D96A1E-6EA2-1B4C-9126-B728471CD21C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5F7C56E4-C298-264E-9CA9-D18D46029A29.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/24B92C2E-4BDF-D744-B021-81D4118722A5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/6856EFD2-A15D-FB4F-8717-1ED96D89EF67.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/11330525-CB16-D24E-AD7C-E564B9469195.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/05E24AA0-E91C-0146-AE6B-AEAFF64D4464.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/97917A36-84FF-EA4F-883F-51F4F4028421.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/04C4FB13-8993-4242-94CD-84089FF065C2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/9F01B795-FCDD-3848-AC6E-E9D8C7157C29.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/1B87CAEF-9A6D-CB40-8E6A-462FAF32D7DC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2178FD58-DF1B-6944-8DEE-83F19E33B07E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/354854B2-901B-8B4B-802C-30BFCD4622D9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/4B60E87B-953B-1143-9BDC-96693AC2174E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/06F66544-04DB-D54F-B003-724D4B96EFCB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/E20DC3BB-3E8B-7442-BEB9-4EA48003B7AA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5FD3F36C-439E-D445-B889-0374491BFF82.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/547C4A3D-CF75-0043-8AF6-E44C7D75EDC3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/825DBF06-B546-1B4E-90E0-DABC32FBA551.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/8022D0AC-7311-BA45-A03F-8CE30ED92A82.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/D20CCB22-31E6-1544-8EF6-15EBA6946198.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/B0F43FC6-DC91-8641-B43C-ED9C0BC29BE1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/ACC3C60A-A55A-ED47-96AD-CB3013899DC1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2AE013F3-874A-8E4C-84B3-38033E2BF9A5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/10B48D57-5637-C241-AF3C-12A7DF148E28.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/6A0B874F-A442-5E46-BE2B-1B1D8A8B559D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/69EF9B56-D43D-F747-92E5-9FAB4ECC3117.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/8A5D5D7E-6120-EF44-BF58-A5CB514A1F82.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2B1888B3-574C-F448-9207-522199062A88.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/F852BF12-AFA3-4644-8CFE-074FEB9EB6C8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/52A4F536-3AD4-4D46-B25B-E32BE87B3746.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/C7C60307-F678-974F-9EA4-07F998BAB330.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/417AACE1-CBE4-C94A-A801-84589246B818.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2223C13C-033A-4B48-B454-36043B8B368E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/CD3157F6-2EDB-1046-B259-15525BFD20A5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/43248C62-8D77-F247-9DD2-D0887997529C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/22476570-2C44-B24B-8942-ED9798578ACF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2E68A33F-805F-2B4D-808E-812569CA4E7D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/1DD9DF1D-7C76-8B42-BB56-7E984F36DE3B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/DD883E74-9994-734A-8211-7FD0AD69C1FA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/1A03C184-2DF5-A940-8DDC-017C31EE76C8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/EB435734-1375-2940-BF96-C1FCA31076F1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/28E48508-79C6-7F4B-B270-79334F4CBEE3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/1A3094E1-4899-904D-9F4B-4FAC1366A820.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/4A02A8F6-8CBE-BE4F-B733-096360186AE1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/BC14C395-128B-7F45-90B8-07B83E3C2FAB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/CE7B9BF0-66BB-7C45-A22B-18EA49F3425F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/080ED470-1644-0540-9D10-21C082F6E4DB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/F1273194-30E2-0746-9172-78704AA523AC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/4B1F6279-9671-DF42-960C-BDCFF1E4DEE7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/855021EB-A3BE-8248-9047-ECF55B1AD9E8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/C8E57B54-D7EE-BB4C-9976-ADDFD6E59D33.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/74AA5E20-A1AA-C24E-B5BB-38A408E94495.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/C17A2D2D-C3F2-2947-ABD8-BDE75714BB7B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5EAB5B87-69FE-A141-9C32-74B85977C7A1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/48ABE929-30D4-734F-A2CD-EE5947D4589B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/65E1021A-4EAF-FC45-82EA-74F69CF27DDF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/16317236-66B4-2F4F-AC07-EC38D731D4FC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/E09AAA44-A06A-354C-ACFC-2AB1DA9673D9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/0862C1AD-D4E2-EB45-8217-CBA2087E5464.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/DF30856B-0748-2C45-BEAF-3966E2A44748.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/F237FF41-F17E-7143-86A2-FE31087304A0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/8683A66E-7EA7-9B4C-BE3C-E48A127C7CB4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/7FC4BE66-D534-C342-B320-36E37043390B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/F39C0A23-F452-7C40-867E-D18A7628D670.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/D47AC134-EA6A-074D-B3B1-E60CEEA60F90.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/67BAEB32-95EC-D540-826F-33B5192986A9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/3598F29E-9421-8F47-BF8C-FCD80452407E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/C66F839F-E0E1-1740-AD68-82E234575E5A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/F6893FFB-DE4F-9B45-AE51-E1D431E0E248.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/E6EC9B58-028E-E746-80CE-224BDA3BAD28.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/846CDEAA-6F55-1846-B3AE-7EEEFF2DECC4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/40B1C009-3B09-0D4C-8579-5EF9EDB68A55.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/50ED2860-794C-F744-BFEF-6DB8E6B045F6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/43324874-91D2-2041-81B4-0F05E5096F81.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/20AD4701-0568-E547-B39E-5071358B906C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/39E7EF7B-B102-CE4C-B468-E1246A9165AD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/3B85023B-64E1-AA47-9E5C-08B5AC05877F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/A4DFB945-325F-D642-BDB1-206B06149B53.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/8D35431A-1174-CE4D-B93E-24114A692DFA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/48EE810F-088C-D640-BC8B-00834EB4B6B7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5EE8B3C4-80C2-1E4C-9A44-08459DF808C4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/02933366-9602-914E-96AF-AAD03DB171FB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/0F6185BC-DA0D-494E-98A7-4D21D073CEB8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2918016C-F12A-D249-8CD4-8DEAB939C982.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/0649CC8B-1155-D34D-9F90-C8585EE45593.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/4B3FE300-B8E8-8A4D-97B4-0B3478E021C0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/DF95F9C5-281E-CA49-A27D-4CDF89AE5E70.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/8D7C05CF-2C37-0642-B4BA-7D59FA802ED5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/A8E90509-3FC1-A947-95A6-02ABC7DD6187.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5A90884A-106E-5642-98CD-9923A4FEE7C9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/B0B60EC7-56BF-6C44-9BC9-542511D97159.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/8CFC9921-981E-E74D-A977-FE160B4DD7F9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/9CFCBEBA-F186-C448-8B44-BF6B9989A4AD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2855E503-0B0E-9144-B6FA-13953A755D3E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/309E8014-5CD8-5846-A3F6-F656A837F71B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/6DFB2E1E-E0BC-474D-8CE6-769C904ECB64.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/818103D2-91D1-7143-B34D-A455CF3CEA4B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/137EF1B6-9CE0-0C41-A8E9-3DB398EDA9EB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/BDEA3981-4645-F84D-B9F5-88467C61222B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5470B2E4-4143-B54A-B2E6-D7C9DFB7B182.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/FB4A1073-03BE-CB41-B7F3-B3346E935254.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/8E11C13E-6244-584D-A3C8-1854082B9A55.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/B7D37748-06BF-2745-BE4D-4BB5A2347472.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/95788D00-28E4-8944-83CC-744C14BB1FFB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/26F52B8F-8ED2-3F46-83CE-18A2BBDB25CC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2433792A-89D0-4E43-A005-C3AD1568AA68.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/9CA1F835-BF1C-D34F-8637-1F8A6694B9FB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/7D8F7CED-0D7C-254E-B933-B76B4E882AEE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/EA65D8A2-92D8-EC41-924D-FFFC6CB23CA1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/1894CD0F-0317-AA4B-B024-9C65D2D7626B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/C4BDAFBB-DDA7-1140-8B3F-5224E0D976FE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/E14CFB18-774A-E146-A293-B6A5DA8F140C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/A662DDF5-F46F-4D4D-B3DD-6D227DFEC09C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/331768ED-BD61-8049-8439-CDDBF02B66AE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/8B55D1E1-30F5-CC4C-B106-C9461E4D20CC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/C687FAD4-0B7D-F444-A429-8C19D164D191.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/BC17D493-9022-C841-997A-C320ECD3A9EF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/58FC17E8-6E63-4E40-B971-63D050DD125A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/CAB0488E-D31A-FE4F-82AE-0107B8991156.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/69C31E7E-72B3-7F4E-8159-2C0D2A9166DD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/31762043-E72D-D543-B4E2-907C31092EA1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/A2560972-197B-3D42-9CDB-46F80C814FAA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5F0D3FD8-E7AD-E841-B1A6-4EEBEAEFB685.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/230AFD18-A4EF-8946-BA8D-403CFD4B2E1F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2AA82A16-99B3-0643-89B0-D45ED15D7208.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/476D2D1D-F1F2-3846-834E-2C04FD812FB9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/1E551066-B6FB-3341-B345-DFD6A2C19102.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/CFE1AB01-9AAB-024E-B101-645CEE9DA797.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/48611BD2-AC4C-A048-99D8-7F692F6542FA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/EEFB8862-FC47-7542-BEFC-D3D774D971AF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/6C2F7607-4D5F-9C42-99C2-76055A6C3976.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/F7B007A5-DD74-1947-8ABB-04AF7398D28A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/5E834DED-E90F-D04C-998B-4446485D7B0E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/448236AB-1798-FB4C-BF11-B07DB62653A0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/1A417BD1-E07E-3D47-A793-7CFD0E2B5401.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/D9208186-0AA5-4541-AA7C-42042E602658.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/52299AD2-11FE-D14E-9B40-D6271F292FE4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/B2371FE8-8C0A-D441-ACBA-3FF650F941E7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/A5AF91F0-648B-7A43-8C24-7C9455779F69.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/FBBD5768-FB38-724D-8CF1-B208DD68DD58.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/3605AEF0-2DE2-0143-9269-F3911EB558AD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/B54F294F-69B6-4D4D-B66B-A8C911FA2140.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/78E69E65-73AD-4946-BE21-ED3E07F3E3C9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/1184E36E-FF27-B345-B2E8-D287F038C7A7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/EC36C5A0-B592-5C42-9D9E-4279A4ECCD1F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/EFDB2E26-88E5-764C-9108-BDE17B70EC36.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/3C058D73-3D6D-BB4C-8630-78F0FFE90B42.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/A2BCF3DA-EA87-2B47-A544-21CB1785D727.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/2B0D679D-A5E5-3A45-9BD8-E07953377E7F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/0A5B3826-1D67-4D40-8398-6E35A36AA92C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/6A265B31-3E2E-B246-82F3-11BBAFC14B2C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/2397009B-7A35-854A-A708-98D1A41C3293.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/5B9ACDAF-7C5B-CA49-AB9C-6B2275BB7443.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/2C5BB026-38F4-2D48-8F4A-A80FDB56AA81.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/F4FE8230-569B-6B46-976B-49B74C808A40.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/1692C93A-418E-5549-BCD7-20B8C1612CBA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/13F44241-0B19-824E-893D-B5B5D09A5D32.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/E598B6EC-481B-194B-9DE3-FBB7B9ADC137.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/A4045B24-6308-754B-916A-DA29DD277B95.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/7F9F4BE2-173E-F645-AA45-2B7AAA695D5C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/95302EB2-97D8-3648-B369-032C4694785C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/70637720-4196-5147-B02D-4D3B3FBF600D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/21566E83-75D7-2D46-8979-CACA2B3FB888.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/7731C3B1-194A-D940-8391-E86AA69EF44A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/AB73D757-27E2-BF40-A5DE-A786B63F6BD0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/72F97F02-A810-CF40-B9B6-818731E92946.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/D076F460-1ACC-2B41-A3DE-1DAAC895598F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/3FB08EDE-9ED2-6547-B710-FCF8CAA094A7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/36D91AF6-D8B5-9849-BCC6-3BBE73557481.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/106CD6A8-16CD-8F4F-85E9-DD19B7D5420D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/C3D641C8-9EF3-0E41-B891-A753948422A7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/AC274D3F-ACFD-744F-BF3F-D8EE98954749.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/F70DE4A2-3C2C-CC4C-BFDB-7D26FAC93FDC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/C27E7448-462D-BB48-AC94-8C5312B6D3A2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/ACE74E74-A213-AA4A-9365-D80557709F16.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/49A17528-BF1D-C346-AC81-194E69B11B8B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/73B6F3BC-311A-1340-B3EA-4E016F742FD0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/8EE53BA9-2156-2C4C-A1AD-2E2930B8F60E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/256397AF-972D-F448-8239-08BE95A5FC03.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/44E82365-B7D3-634A-A092-E89A14A52910.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/271E932D-017F-7C43-AB65-70D49E4014D9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/62ED996B-1B02-A04E-9902-F4F7A587246E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/E861FBE8-8406-4D40-A59D-2119C7502252.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/F6484F41-7AE5-7248-A0C4-8AA4E286F359.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/65337F45-A124-3645-9A64-DEB1F29DDD6E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/07F9B1D3-3BA4-E54C-BD3E-521EF0068CA7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/F5D46826-0901-014B-8943-236404088183.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/6A77C2B1-4203-CA4D-B4BA-A163C8FD25EB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/933409B4-1224-4C43-8CFC-7CD2D1C7F02D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/95A87FC5-4B26-8B4F-9E78-09E00170A4B4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/2069FA47-5001-E64E-B07E-7B8A62587A74.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/CD4A44E5-493C-304F-86DA-6547D566466E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/2E1726AB-3E93-BB49-AE6D-F4BC7F74297C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/FD63A9BB-35A5-1C49-89A6-B86DA26BCDC3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/C3AAACE7-FAA9-1646-9C5E-0C7634363430.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/5BEFD808-3635-1544-9F60-DDF420DCFE53.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/A20ADAAE-A648-0B43-A24E-00FFC07657FB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/8FC570BC-73D8-F940-8709-B58492120EF3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/A191E6B3-463D-1941-BB05-7C32325C9235.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/4F9FBAF4-0ECD-7C46-AFDA-F342E75C4E3A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/611500F0-9B68-B643-8BC5-1DEA6F2FA141.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/265352D8-D02F-ED48-9C20-11B8B402873F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/9C3CC83B-7F51-B942-A760-EFD29D9AEF71.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/3FBFE6D2-1322-5E44-832B-94C32DFC09C8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/517F60D8-9592-1B44-A056-FBB93FE021FE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/FAC2849D-4A83-F64D-85C0-F7CE3F6E105A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/6D9164A5-478D-2E46-8589-3075AE9AF0C6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/1EA2A660-07DF-FE4B-A725-AD310B1E385D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/C4722F38-C3F6-B744-AC32-DE8451860363.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/A9890C9F-FF62-A742-A38C-E50361FA7BC2.root',
] )
readFiles.extend( [
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/80B1CECF-6DC3-6F45-B707-9D7B5A66D1EF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/9C112783-8C8C-A04D-BC9E-4F8D25753DE2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/EE007BBC-80AB-3B4B-8425-5A8D8A91E82E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/F2FC5E64-CB9F-0C4E-B572-17E2FF1E9B7B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/1C970598-6B44-E348-A1A7-345A4FC9FC3A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/4D42FD37-82DB-1A4E-88CF-81C2AD7288AD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/D186A3A4-E8FC-D940-9A4C-EC11981B85AF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/282FF9E2-AC92-7D4D-BA8E-1BEBA5942059.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/D58DF0FD-BD31-BA48-BACE-4BDF7847C58A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/805515A8-B6C5-B041-AC2C-5DA6A0761280.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/8BF2D6AC-2C2B-1942-B1E1-D99710B6735C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/DDE92677-28CA-544F-8349-03C95FFFC113.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/4871345E-6C73-AE40-AC65-BCF68831A2DA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/AD4FE8F4-07C6-774C-B2B5-9010999E1A2C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/7D7A0040-D13D-1B4D-B3A3-417EB4AFC87E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/F2A99C89-D21D-6044-9CDD-0E9370BE63B5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/1A3B2A83-55A0-C541-9C6B-666057B85522.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/AE35736A-0566-3C4F-94D1-7088DE26F5E2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/34D0119A-993C-BA47-AD2C-FEFDD2477EA5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/6A5852DB-15B4-B74F-93FD-5124211D487C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/5A97C967-AAB5-1F45-8F19-4C66FC63B777.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/1937CA66-8582-8B44-8AF5-0EFD6A58D4F1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/E9278218-7374-C64F-900C-7F21EFD1E52F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/A0DF3EAA-06AD-C64E-87D1-A9B8FFB63A2F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/19C4813E-2C52-574C-B905-B60F6E144CAA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/B61DB3B0-4646-2141-BD69-DFD3404A4F4A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/11127578-1A6A-404E-B636-F50071600544.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/3059E5E2-1AED-004D-BFA1-54E53A85C530.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/4383C436-5720-A44D-B5B1-D2DB2740BF2B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/227AC609-EDC6-CB4A-B40F-856A401321EC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/10472E66-9DF8-3E49-BD4A-43526A7B1F54.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/D9B1860D-3A51-0F46-9D4A-B10ADB7CD107.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/318E11CB-4307-9145-80DC-8F38B6F292DF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/9DE5DDBB-A7E9-B244-B85F-F5CD5428CF8D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5F182CDF-C194-B84F-8BFB-23AE7018103D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/7AF9AA7A-F690-F44E-830D-AE0CC61DDFE2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/AD28E1AC-6DF2-CD45-AEAA-563D26116E73.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/DBB433AB-99A2-724C-B1C1-027A370BFDB7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/9EB7C3D1-21A8-E64A-A1F4-304534087760.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/29D77B3E-E7C1-9E49-BE4C-68AC78D1EE4B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/4448DBA0-9F25-F144-A818-BD69C819E92D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/C600711E-286B-A14B-8C38-91D07CC4C780.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/E563C971-02B5-1A47-83D4-8E953DD87EF2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/2BE9CD3E-E51F-884C-B395-38CBFF97FC44.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/044C2D99-B3D9-A947-9C5B-9FCD049766D2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/8E1D65E0-336F-C04A-AC8A-7F143E3992FF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/DF6465B9-BAD8-2B41-90C2-AB8702EE2D66.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/F0ACF9DF-7F89-5446-95BF-5722BBD13546.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/06AD5AF6-98F3-174A-B8FB-6834B2A66BF6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/405289C4-BBBC-3E41-ACE6-B76FE0408E71.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/6B27C285-BAC8-4146-9E88-1CA5D3301063.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/C9A4F103-68FD-6248-9416-068D8F562676.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/1A8A3983-AE72-0144-8851-A4EE539326DE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/7D512377-E3E4-2441-9835-57BDE89C786F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/E8BCB857-F1A8-B14E-8553-1DCB7BD7EE5B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5239F012-1B51-4C47-9775-DBFFDA6D3771.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/E0E91BAB-2413-3342-9C37-3F1342894B71.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/8CAB4BF5-C01D-2E4D-B880-EFB518A4C213.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/5492CACB-9362-584B-BC35-B66EDEF32563.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2462C223-F4E4-EC4C-9111-9D3CF060D688.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/FF7B873C-9118-F841-B2EA-A51382F14F71.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/90D32E27-01D7-8F44-B896-DAC7F1A5B34B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/71C2E6BB-3B16-7C45-8D95-ABEC970204F1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/C3B1A4DB-7CDC-2844-AEED-63AFEBCB53F2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/11226DED-CF5E-5644-9BBA-60ABB183E31F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/0A52FD78-4849-5341-9F11-30CDF88DDAAA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/554EE24E-6BF9-544E-A6AF-4A26F6A81BBF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/36C8530D-DDFE-014D-86A3-5D0C0FF381DC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/2AB2089C-7B74-6848-9CCD-2DB62CC9678A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/1210000/FD7081AD-BC90-7842-A028-5C22897929B8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/1210000/BF442ABF-D097-8C40-A69D-F5B2BE173E53.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/1210000/1818149B-4DFE-EE45-A1C6-E9C9FDFD0398.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/1210000/54EB38FD-5393-1742-A863-D268B3E912DE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/1210000/F94DE3A7-7030-9B4E-BDE1-639FCB22AC0C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/1210000/0414CC9C-303C-0F43-B967-1A9680983E5C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/1210000/6F1BC67F-3E94-8441-B0D8-3585E76F012C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/1210000/129F01F4-DF32-0A47-B6B1-F50B80F99B46.root',
] )






