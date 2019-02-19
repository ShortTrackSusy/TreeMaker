import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/038247EE-ABF3-3B45-B73C-47D7467E73E5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/3FD7324C-7DA0-754F-B990-D9D07C6B9D3C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/AED0E698-4153-1748-A057-53A61E6853E9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/56F5EF2A-954E-2141-92EC-F1196542AE92.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/97A479E5-7EBE-244E-BA1C-58571DD89E2D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/8D95FD05-CD4B-CF41-B2A2-C06E956584EE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/5BD429A0-D1A0-4D48-BEFF-2C9FF90EDF1E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/4D799F7E-09F9-804C-90C5-1473AF10FE26.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/D6A869B2-489F-8C4E-8F88-15A8C26B9672.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/16251D3B-842D-E44D-9052-61AD6206673D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/26016A72-E682-9540-B3C4-85E0BA8CFAC0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/084A0D7F-4E65-B34B-981B-E10EF6811662.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/80AE3D87-69A8-564C-B081-7217A63DD565.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/DA580A47-FC48-1549-A744-77F1AA767BEB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/992E5FE8-54C1-D249-B347-ADCD88C95FEA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/B1C7EA12-132C-AF4B-A433-B11D3E6D3336.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/6C3A9934-9187-364E-BE66-F53B5C7C08FB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/ACEB372D-6651-2B46-858A-C506B4D997EF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/13CD97B3-606F-0A4B-B8E6-DD1F782E00E1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/B1CE3FB7-DB0D-E843-85C2-4BC0D88FDFFD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/46B7B2B0-86EC-5D40-8DFF-882D4A8CC90F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/5201E430-F947-CA46-BF3F-52D0B4CB3473.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/A77AA4B7-E7DC-2744-9458-0CECE71F8A07.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/4D31EFDE-C7B1-A043-9CF1-3FB5DD9B0EE2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/B8C39652-803B-8D49-B545-59279E25A31A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/FA9B335E-33AE-E047-BD01-628310D9916C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/938464DE-B6A5-2249-8BFB-03B5F56DC7F9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/6EE2BF4B-6EC3-2F49-9057-F5202730C846.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/B5D6457F-B31C-B74D-9A16-F1A38CEFDE60.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/76DA3D40-D439-C449-BD7E-0E33E3483D41.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/A79FE116-8C2D-9947-88E6-D0D7836F8C3E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/E2835ACA-C92B-734C-961D-8C8FF65E08EF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/712D42A2-2A79-C649-AD40-5A4A9DE38E69.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/9829F48B-4676-8B41-B210-FDF3B9D7D036.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/97E11443-5877-874E-8F81-3E9EA36C0AF6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/2C112AE8-D010-214D-BE98-7835941B4184.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/1F16C81C-13A5-BB4A-BDA2-3338FF224233.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/B821024D-D15E-7442-820D-7C571BC5613B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/AEACC25C-EC9A-ED42-AAC8-4888FB533546.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/0A81469E-C63F-9242-8531-D324F8C80DB8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/B7DD3C86-269E-EB48-921F-7715FD1A42BA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/0F055B4B-6CFF-CB46-9E10-9ACDF533C37F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/79FC859E-9BBA-4142-8664-B37D2C9F4A37.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/6AF84837-D11B-3145-916E-D221922735EE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/AE3D4826-4D2A-A640-A190-F91942169865.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/5162295F-B174-7043-B00D-B10541FED9AE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/D52BA3BF-5518-7648-B194-6D2D7BAB1843.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/39FBC949-948A-2441-B2AC-15724BD6D889.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/4E717372-A694-4C4A-90C5-EFB080CCBC3B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/24F6CF8E-E7B6-654E-B4ED-531FC56455DC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/2ACEE6E8-74F0-8142-80DB-5AF1A935BBA4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/45AA31B9-68BA-664B-B782-A5BFFFA05CB0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/31FF844F-8FE6-154A-B209-472A63ECCCD5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/5CFE737B-DE73-1246-A518-A0C287E38F6A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/A990F4EC-4089-3344-9DEF-1A5AECCD98B8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/2D2683AE-AC86-9E4A-B18E-44F4A0281C87.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/2828D5C3-AB18-6D43-8C68-91E085650DF7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/A155BDB3-FEA4-1A40-8803-FFC25A8C9875.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/FC8AF265-0A75-9545-B07E-4C9FFF538393.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/51482AB5-EB70-E64C-BC30-1A5A018C7C7B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/35D1C9AA-055C-3C48-A383-2D35C72F426D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/33783FD2-C3F2-3948-89DB-D199A19A9BCB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/D92FDE4B-C3F0-444E-A5D1-D9363D0F8926.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/F5990E7D-B0C7-B443-914D-21D760A927D7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/1000E04C-608C-6541-9D29-0CBAE0A87656.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/55062957-AE21-7742-B2AA-E22FF8004D41.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/CDC6EAAA-CCB4-2548-B24A-290ADC2A22B9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/CBC00FC3-9946-6940-976C-B35D6D426F72.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/5D962B90-8E98-9D4A-ACE9-6C0DEC967D0B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/E03001FF-5C2A-8F40-B182-A9087CFDBE02.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/9F88D2A8-8A11-9046-8E61-0AFB9000971D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/57562439-F10B-154B-8F6D-78C3EF398136.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/D157C4F5-AE5F-024A-8672-A4FEC7D047E7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/3AC438D7-1317-C64D-AECD-6874D5EFE7ED.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/A090139A-D477-4C4E-A554-DD6D95896732.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/987B423B-62F5-5542-9F13-2725FFD8B4C4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/35D84C09-AFB8-C941-BA41-90D10C9D5629.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/CFFA2672-6B7A-E04B-8698-20F70D25C630.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/E24EE05F-824E-4541-8D60-E80287C12009.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/1C59D5D5-1093-F045-9778-6D8C235871FF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/A2356781-3104-914F-97B4-8D3AD59905D7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/8FF606BD-F1D4-CC4E-B116-BF089D752F96.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/A00EA571-52C7-CC4A-A587-01B693432EAF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/9BF90D56-E4DC-C84B-AA5C-2956A5CCD722.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/2313E98A-B609-F640-83CA-62E9C119BEB5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/624B4DA7-7B1F-324A-AE9D-41DC3EA85371.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/03537F53-9786-6440-9A36-436B2533C5A1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/AABE5B38-9074-8648-B4E1-5D0E9C9F539B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/E984583D-479F-FF4E-B9BA-906001AFA643.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/49AA3252-377A-384E-BE75-EAC2E3400322.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/644EB637-7DB6-5642-A971-623D9C2CD6FC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/98B6F354-1C42-0744-8CAC-2F44A4DA41B0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/728673A5-5505-124C-BF0B-A86D07F05EB2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/D7586AB0-767D-F24B-8C7C-0B74F7971665.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/0FD3BF36-D7C3-9542-870F-AE22FF13B6B6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/DA437F0D-E23D-6E42-82C5-026C3D322F38.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/481F1CD6-7D3F-CD40-9597-2B8817467DD6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/04309064-04CD-CC4A-8FC8-B0D8B308622D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/1AAE7D77-942E-664E-A009-1511CA55EFB1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/EF309A0F-4C72-C246-9897-B82E56A5B0A7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/AAFDE5A4-B737-5D47-AC80-B6718530DE99.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/E01C8C42-1F23-9A48-A50D-7D9DE27EA628.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/E44ABE9E-33F4-A440-A46E-DF086E9D50C3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/8D277D91-5888-2E45-878F-BBC7419622B3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/7C98F7F9-2EAE-894C-A39F-8CDB31F7E22D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/C4976461-7502-C842-B699-E16AD5AB2959.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/03688EE2-10BC-1B44-85EC-6543847DDBAF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/853338C5-FD42-2646-96C8-8F9C7054D2EE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/BBB7CC9C-FAFB-2149-A558-76BB077B5344.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/F60962BB-BA88-3748-AA47-ABF4C0FDFF51.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/33BD8C37-2EED-8941-A3E6-7E90096826AE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/5F460F63-FB19-294B-8676-3D24F647AC73.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/D89EED36-77E0-6649-BA71-A3D3B1400016.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/41F1D51D-E409-D246-B306-130A8E8CC4C8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/3151348D-A3D7-6348-9C49-10738693BBB1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/6ADE3AB8-A349-C443-893A-2269FD8AA5B3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/91893987-81D3-9E49-A94E-CD73A5F6098E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/6E795F50-5B63-DB4F-98A8-9AC0E3B9EDAE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/001D9E14-4108-974E-BE87-B1AF69B20D2F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/6ECEEFA8-F202-2C4A-A921-DFFB996F3656.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/E5672B7A-3C7B-A147-8081-81EB3A2EB894.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/F6FE6614-AA11-8B44-80FD-9F50F9A1D35D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/CF2AF520-170A-5A42-B9AA-2402F3214574.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/96262401-0AD4-0A43-BFF0-75ED7C59464E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/6742BF3F-3E29-474A-ABA9-9754DB83D02C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/B0ECD8D8-6F03-1A4D-8ACC-05DFA3FFEB3C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/62DF9554-0967-6346-A233-1AE54C5A8052.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/E55B5F7A-DE34-3945-9E0B-41B2805A467A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/FCB223A5-6424-044E-8D17-DA487153257F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/F3B5E159-2567-5742-B9A3-AFA89F4342D5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/39F2F0ED-9107-F44F-B786-B62678D2EFCA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/47CDD18E-56B5-2E43-A472-80ABBC758C73.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/2617F0C4-B893-1048-BD32-7FFB03C7800A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/4C7F5470-3244-E647-9A4E-8AC631933AAE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/8A876C7B-B9E7-464C-9B75-9877BF3E57F3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/EF414A39-B96B-704F-A241-397DF67A00CB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A573BD9F-1DF8-BD4A-B07F-EBCB2EF0A669.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/87164777-B1B3-FB47-BCC1-85919CA1C4E3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/F63276E4-7DC0-F54D-BCDB-62B5BDBA3887.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/96547412-98FE-6647-8695-F9CBEB2C2A95.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/0E6B4A98-5C49-D640-A609-970B0AEED927.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/28BAEE51-5173-E34B-BEE7-EA54F91FA485.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/9134F9F2-CA6C-8B41-96EF-7DEDE1A65700.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/8F016DAE-F528-F141-853F-C64B06D2FEC1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/2064CFB8-6B62-2641-8A73-6A2D39A1920E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/2FF8F65B-859E-204A-B70B-42B3B884EF54.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/05C969DA-DAF2-FB48-8AD1-7D8F45BCE0A4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/B09207F5-7830-7047-AEAC-A946FADC5C72.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/140C63F5-D96D-0E46-A30E-51CE2727F9FD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/5EAC10B4-86FB-A14F-85CF-3A27218B68B2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/42D9222F-3822-C44A-B647-C540CA06884A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/40E24CB8-3D32-E140-8C21-1AB18C469A5D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/204B1F91-8E07-CB49-B29B-ABF1907CC4C1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/87938D0E-689F-9640-91F2-A960FB3CF458.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/ED92F795-6EF4-7749-B80D-A9ED66ACAC97.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/BCF12274-DEDE-E642-9C6F-F90977B049A3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/70CD0AE8-475F-DA41-B01D-926364B0FA7E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/8F9C49E3-9281-6942-B98F-86D7077E0459.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/2A6741A6-603A-C04D-A9E8-D9A1139C718A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A8D1EDD8-8AA0-0346-ACD5-CBA28E771894.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/DB6F3A9E-41FE-7440-BC71-685604AC849B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/5DC76F59-0F61-3D43-8CAC-D2324A987C23.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/35D16778-4CBF-E643-A1F9-F81EC5241DC6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/CE90985C-32B1-DD4C-B5CA-32B7CEF87929.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/1AD46517-4E12-B44A-970F-B9849CA4595A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/7F187C99-6821-894D-AC73-797F8846A0ED.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/DA152820-6950-E848-97F9-3E5E4783B7B0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/76F8590D-BB55-4444-B5E6-31176D4715D4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/67098FD1-C790-D441-B6F2-4EFEC315655F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/017D7C8F-2DD3-7547-913F-B092BA06AC66.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/37A12E29-BCF2-6B43-B754-B8EEF8C8CF5E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/1F93E22C-0182-E84D-A65D-BDDCE475A8F3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/5D8126EE-331F-D34F-93D2-F0C74AD0B1F4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/38BC0867-BB91-5948-838E-4024D073050C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/6DB8C13C-1E5B-2246-BE93-F5A8846AED53.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/58E5BB85-2CF3-8541-A591-6A4B30F83E66.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/60913358-2E24-1948-A6DC-E5D299C43383.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/C8B84F23-4295-3D45-A0D7-5BD112C5DF7E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/29B1CDAA-466E-6942-B0E2-EE43C905724A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/1729C29B-6CE5-1C43-A757-0EE54AA52FBA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A80FCF1E-078A-8A45-A355-95DE6F1D3E13.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/5A33BD24-1B09-D24B-A8EA-8D3C4E74B53B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/FE7C9C7F-3FC3-AD42-B61D-5BF8D081AF53.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/DC689281-2C87-F446-AF79-E31875250556.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/E5AC8590-06B4-F84A-8E82-85359E3CCF37.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/0E67A74C-8F6F-2849-888E-CB5574D9F258.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/9A2A66C4-029D-D14B-8CCB-6C79FD3EB8F3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/871FDC79-5DFD-BD41-8C2B-0E05E8EEFA90.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/9488FCB3-333B-2D44-8FFB-E25344026750.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/14CD2C09-A2CE-8A4F-9477-C47626D150A7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A34AE2B7-29FD-4C47-88B7-80DC14943134.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/1998BCF5-D808-064E-91C1-EA0EBBB3D0A6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/05D8C3F9-23B3-EF4C-A2E5-1F8CDF30721F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/80A2A1BF-E4A2-2642-96F8-CB55BEF488F5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/03BA6307-B5C6-1048-AC87-260379529C00.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/4D49F646-C313-2D48-8CCE-C5F8E2761343.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/905671BF-B86E-1142-8133-2B311C423DBD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/FA9BDAF2-DBCA-C547-A2A1-B61D5E432DAA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/AD3B8174-6CF9-CA48-BFFB-1FA860FFCB21.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/3E6780BA-D1AB-5645-8801-D3CC5F9F60EB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/EF8D81C7-89FE-2A4E-B820-CFBDA80665FA.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/72B8B671-B26F-AC4C-ABCD-259FA8D52738.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/C6A3B5B4-B9BB-6047-B048-EC39B8BE9020.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/B8F94F7F-DDA4-4B42-9A2F-B0893739ECC5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/72684B9F-3AFF-BF47-A153-C90FBD5B5ED0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/72AEEE7C-D9CF-CB4B-9FB0-A0632C945A1E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/55912E6C-B3FC-CA48-BBBD-A772468CCC14.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/B709D5A5-19E8-4144-87DE-A0203CAFAD42.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/9BCC501D-0358-794A-8F8F-D1C58CC1F05D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/8C8BA2A9-2C7A-3148-8560-1DF3C7043EC9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/1D917CDE-16A0-C64F-9002-4EE19C85C94D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/37815D41-DDF2-5C4F-A07A-72335E173355.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/8B36BF8E-44C4-8C4C-915A-01D48A0E7C5A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/F3D002EC-BCED-2444-99F9-F28C492C034C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/8D68452B-67CA-BA43-B321-447AF9A90949.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/91606D06-2FE5-804B-B3E7-4A841F1F9DA6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A9E16B25-1A4A-DF44-95CD-CD8B478B8FEB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/E74D7F4A-63B3-0D4D-938A-EFBA087C7E7F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/7AD965DA-41B1-B74E-BBD1-823BF0C7D903.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/801F8C46-6A20-C54A-A9BA-CE62ACE2E779.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/D7F9947B-75C5-CC45-B16F-99F4B4B8545D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/8923FB4C-B403-BD4B-B62B-D064DF12C707.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/82D67C15-F6C7-214B-825D-1402C9F76894.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/79F0FEC5-6203-EB4C-904F-0BD11084127E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A2EBC3BB-5676-E045-9700-7BE58F3471A0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/F72D5875-B48D-B24A-A72B-AD4360A54839.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/52740685-BB9D-794A-B323-B8D75660CE2C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/3CFA9789-56B0-414E-9822-7AF3033AEC37.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/AF8857C0-6E05-BD46-AE72-109C5E30F4D6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/84E077D6-30E5-5746-88DC-78FDDB240435.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/DD8E5693-D7D2-E448-9267-64A3F50BF9DC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/97BD936B-2FE1-B440-9689-298682E1C5AE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/282D64A4-AC71-7B4F-8D20-C26F3574A5FB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/4517BFA1-F920-924A-BA04-BFBC63821A58.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/4BBBEC8E-3AFF-F64F-A2CE-63A453A926EF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/802F1446-53AF-C845-8326-8B4D253D12DE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/420F51B7-CE21-0D42-AB9F-E99FEF5DFBE7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/C9425137-72AC-034A-929F-1673874C6A63.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/5453FA31-CEF8-D54F-B5E2-41560E443466.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/0BD1473B-70A8-4042-9194-71034E8F9E1A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/667840DC-959E-1645-A33B-43F39DD93767.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/6F370BF4-BEFF-BA44-A8F7-056B32E7034E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/2DD9A73A-7B29-E342-94FE-B627E85A6787.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/40791980-F669-0A42-BA6F-DBC3CD427D00.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/936F79A0-6DA0-6445-BC25-03A54F2535B3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/CE5CC598-06FC-734B-AB2F-7350F5EE65B4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/F7979C09-6540-7F45-9D8D-36B9C0AA6AD5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/3723F417-CF4C-D841-8F45-D776E6A068A4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/AC6F7B01-722F-A342-B056-9448729320E8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/5484A78F-6249-9D4B-B2CC-DBD040D757B5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/9FFD5424-FEA7-2043-BB64-96C683B7B8C3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/E13CCF7C-5927-354C-88BE-C789CE644CB0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/35292CE7-711C-AD42-BC21-7D9363434CF3.root',
] )
readFiles.extend( [
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/182BFC8E-599F-2147-991B-28330B3E551E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/180B92E7-659D-B241-BA90-36E83DB840D2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A7A0C73C-C9C6-DF4F-97C8-DF798FC37203.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/0B3A62E1-1AE7-5647-9338-D635A0030C15.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/790C6EE0-734D-E94B-A70F-284E765F708A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/9B8DA0A7-FE5C-6649-8A5A-F526A121A4E7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/85A2B380-6F5A-C845-907A-675FE9BEF4C5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/05C3E336-8B0E-794B-82C0-4F7B512A8655.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/817CB82C-90D0-2F42-9438-52170791C835.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/D30C46C0-656C-124E-99F8-FF617BB975FC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/C6301208-B9C8-A546-9A25-E24C424C7673.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/FC1551EF-4C7A-8B46-B3B6-9A9DC709C6A4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/2A833839-F686-084C-B753-DE17071150EC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/4F3F6D02-3B0B-FE49-A156-7888D1E268F8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/FFFD5038-F4F9-0345-810B-1124DC5089B4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/B77236CE-5BDC-4943-A1CC-9D19218B803F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/11A158AD-2A7A-6E4A-BBF0-60019CCDE817.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/B7AD05CD-DCCB-CF4B-9626-EB91A17ECE03.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/DAE8F861-2158-AB41-A3F0-8884B2C86047.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/DFD2997C-C68A-E748-B5A8-1A66C302A7B6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/18BABBB6-4020-634C-B962-44579D7D8413.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/941CD764-EA66-A248-83FB-F2D9EE76B67A.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/23971642-86C7-D341-9296-D72F64F61D51.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/821C70E3-3877-164B-B655-2B121CC5D526.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/C7363650-5EE7-1043-AC0D-3E56D2368B56.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/F9958E1F-3AD6-5044-9CAF-861E45A98E64.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/29D97A9F-2CDB-D542-B1CF-BFCD99EA5966.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/70D49006-0A88-C845-88C9-9F0FB2746815.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/3B10B08B-69AB-6540-9FC0-CB26A6553907.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/60000/4667CFF2-F340-BD4F-8394-85452104E518.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/0B95E209-28F3-3946-8F52-5058F8F4A353.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/4B549F33-0D20-C347-9D30-CBF24B893A11.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/AB70B997-6F6C-8641-9321-F660A9F551B9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/5DCCC480-2315-7849-893E-A8E194C06C2D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/FECD9CAD-5FEB-4847-9BB5-28F24CD092FE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/DD773A4F-4838-A347-862B-AD0F7E6E649C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/1BE83A6E-93EB-5843-B02E-4D4E71164EB8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/DEF60D65-19F8-864F-B3E4-4F81BCFA15F1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/EA29C437-03E6-AA49-A851-A79B179FBACE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/056B2897-D008-F344-A995-343DD2D30017.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/6A55E2B4-F2C2-C848-A9B1-91F1738E99F2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/7612203B-D9A9-EF44-A6DA-CD8EF4C6FAF3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/5BD7F22E-37CB-D947-A72C-D55FE76BE48D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/8A65026D-5EE9-6144-83DD-BC08446574F4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/BB39C1A9-E2ED-984F-A2DA-415C52963A3E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/74C2B617-E81F-7A44-AFDB-6AAFD2463CDC.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/44D25952-2046-5B4E-9FBF-2825CA2E1A77.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/4E1CC7B5-BFE2-8C4C-B120-655538461C5D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/6FD43D2E-AAA7-B64C-8C90-433216E61A8F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/8223FF6B-E41B-6143-9F4D-ACB9CDD238FF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/0A6811D6-D8BF-4740-9B94-916AE46850D5.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/7A686DD9-7A21-1E49-942D-5B21A2923A61.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/4CFDD91D-546A-3547-B516-6C4B0DB0774D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/72CD25EF-5FC5-3648-91C8-1593AB362DA0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/6C9EDBA9-36ED-EA4D-84BC-27F95D28B49B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/3CB7E975-69A3-7F47-A433-4C65867E5B29.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/31EB98AD-34CC-D742-84BA-3CBD2072201E.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/203E0DB0-2FF2-9847-920F-0E9C5144CA33.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/FA77895D-28F7-0149-B754-2DFF2400FD7C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/E959566D-11EA-AC41-B242-21CBA552102C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/D736A59D-FFE5-A846-8FFC-7B8397942C18.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/7A0C9C54-E8BD-074A-A5E7-9790BB2FDFD3.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/F0CC448B-3D36-4E4C-A7FE-8393485A5EBD.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/7AA04EDA-D3B6-3B4A-9204-E979D3C04E1F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/72AF8262-723B-8544-9C7F-BD994CE57CD9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A7FCCECB-3518-6248-B23E-D92E393DF9F1.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/856DEADC-6874-D140-A1EA-B47C9B10ABB7.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/3B1F216B-1E1F-2647-8004-8F0A5F82F276.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/32CE63F4-53CA-DB45-A106-AAA1A6BF54BF.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/98AE2193-85B7-3546-AB30-8A4E193225F8.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/623B2DA3-7EFB-454D-B49F-93F24A26FAA2.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/1FEC453B-BD53-FD44-ABCE-96EE1A6E40DB.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/7F1381D9-FFEE-414A-819D-19A6CC540110.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/72D93020-82AC-E242-862C-611A52229C27.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/ABEF99FA-377F-F049-93CA-9C5EDEE22AC0.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/448889AC-3C2B-9A43-9780-BF73D5BF795B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/12E5BC1A-6641-204D-B2F7-BC2F37E1325D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/5FC16E7A-05A2-884A-9BDA-7F306A246562.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/B70EF295-BA45-914D-BEEA-3F507DA39436.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/9CFB99BD-6483-DC45-84C0-1DBFCE2ABA1B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/11CDFA81-D8E4-9647-B515-50460996CA16.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/FB0D7EA4-876A-CD45-8FAC-C88A585E7E4F.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/311A914C-CAD5-6149-A89C-B23D535F638C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/BB5849F8-A3AF-D247-8D22-309E7BFAA3E6.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/90412AC4-4EF3-4B47-9728-98A730AAE2F4.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/963B072D-7171-3245-AFF4-087BAC4442D9.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A9D3C5AE-19E2-9542-AE1E-50F416ADED5C.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/09BCCEDE-A2AF-FB46-BABC-722B09602C02.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/AED1BC8C-AC55-544F-B12E-8D426ACB32BE.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/4F5FFD3E-E23C-444E-8E14-8512365A761D.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/A1DBAAED-EB56-4848-AE07-1E3ADEDCDB3B.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/100000/EB99B8D2-D8CF-154A-BFD9-847255460558.root',
'/store/data/Run2018B/JetHT/AOD/26Sep2018_HEMmitigation-v1/1010000/20921E47-EE22-F84F-B0AB-D28350B856F8.root',
] )