import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/709D75A6-E7DC-E711-BBDA-008CFAC9428C.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C65261AF-E7DC-E711-AFA8-008CFAC93EF8.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1E0CFD24-6EDE-E711-863D-008CFAC91B80.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/507C2DE2-A9E0-E711-A909-D4AE526A0D22.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1C778F6A-FBDD-E711-9F30-24BE05C6E711.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/74764AB4-FEDD-E711-99A3-5065F381A251.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/3403DC8C-01DE-E711-9D83-24BE05CE4D91.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6415887B-01DE-E711-860E-E0071B7A58B0.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/903AA779-88DE-E711-9DFA-5065F381D2C1.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/04742440-6FDE-E711-B53D-E0071B73C640.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/BADA9106-8DDE-E711-83F3-24BE05CEBD61.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D84F21F7-88DE-E711-A767-5065F3819241.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/56147EE5-55DE-E711-8C08-5065F3816201.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/880B15AD-45DF-E711-BEAD-4C79BA180BA7.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/4855F534-84DE-E711-8148-008CFAC91B80.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9CA51084-A7DE-E711-8B39-008CFAC93CB0.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FEFB8031-A9DE-E711-B81B-008CFAEBDC00.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1A69F91B-E5DE-E711-B87D-A4BF010122D7.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1E8F3128-EADE-E711-B96B-A4BF0102A4F5.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6E17D00A-A2E1-E711-B774-008CFAE4530C.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/AE5778AF-C5E1-E711-826B-008CFAC9112C.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/489938B4-08E0-E711-9B8F-44A842CFD5B1.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/688DDBA8-51E1-E711-81BA-B499BAABF37A.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/04C673F2-5AE0-E711-9E95-3417EBE7051F.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/74E40BEA-5AE0-E711-BC06-0CC47A7FC74A.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2AAFF61E-5BE0-E711-B35E-D8D385FF322D.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/64B03E23-5BE0-E711-9057-3417EBE706C6.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/1E83C63B-5BE0-E711-87C4-3417EBE706ED.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9C792C6C-C1E2-E711-8042-0CC47AA989BA.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7697A9E3-01E3-E711-B924-0025907253C6.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6C18FB22-B4E7-E711-97AB-24BE05C48801.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/F45CCD7F-08E8-E711-BDB3-EC0D9A82237E.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/92DBC58D-08E8-E711-A4CD-24BE05CEACA1.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/387C9C90-0BE8-E711-9B1E-EC0D9A8221E6.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/76E5B1D7-07E8-E711-BA24-24BE05C6E711.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/0A5FF79F-0AE8-E711-A8F0-24BE05C6C7F1.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/DEE90ED7-07E8-E711-94CD-24BE05CECBE1.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E2491589-09E8-E711-AF98-24BE05C6B701.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2C201A51-3AE8-E711-A84D-008CFAC91E88.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/94DDF770-99E8-E711-9CF4-008CFAC93F18.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/6E1022D8-EEE5-E711-910E-FA163EC43472.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/BC4E5C8F-EEE5-E711-86FC-FA163EDF53DD.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C48298F0-ECEF-E711-9E35-0CC47A4D76C8.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2E99F219-4DF0-E711-B1DF-3417EBE7002A.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A64D81F4-65EC-E711-BCEC-44A84225CDA4.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/0880DCD1-66EC-E711-8948-002590D8C800.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/8C380385-3BED-E711-AEB7-1418776420DF.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/2C28B65E-E8EC-E711-BD26-44A84225CABC.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D23E9CCA-29ED-E711-8660-141877636851.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/38A39A6F-38EE-E711-84EC-002590FD5A72.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/BC45409A-32EE-E711-A80A-0CC47A0AD476.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/A889CE9A-BCF0-E711-84C5-A4BF01125D56.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E4B84495-92EE-E711-8138-1866DAEA8808.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/BEB89E86-D6EE-E711-922A-782BCB20EDFD.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/CCAE1520-4DF0-E711-9FA7-7CD30AD09C52.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/0885A8C1-75EF-E711-A03C-90B11C2AA388.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C63D19D3-68EF-E711-BF8D-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/AC16BC2A-69EF-E711-BD35-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/046E18ED-68EF-E711-97D6-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/98B46DD7-8BEE-E711-A9EA-002590747DA2.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/CA07947B-EAEF-E711-B2E1-B083FED12B5C.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/B6890995-75EF-E711-8AF5-1CB72C1B2D88.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/E0ECDFD3-29EE-E711-AB97-0025905A60BC.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/D2C37BB4-5CEE-E711-AEEA-0CC47A4D7630.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/4209A45E-6FEF-E711-8460-0CC47A4D76B2.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/66D68C52-6FEF-E711-A837-0CC47A7C360E.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/9278EEEC-EAEF-E711-A4B7-B083FED0FFCF.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/C61813D9-09EC-E711-B398-008CFAC9432C.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/7C990344-3AED-E711-BBA6-008CFAC91790.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/60000/FEBF9799-02ED-E711-823B-008CFAC94024.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/3E8FC07D-3DFA-E711-87B9-0CC47A4C8E38.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/72415D7D-3DFA-E711-A0E1-0025905A606A.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/20000/209AFED1-3BFA-E711-8C3F-0026B927861D.root',
'/store/mc/RunIIFall17DRPremix/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/210000/5C6FD973-1EF8-E711-A674-008CFAEBDC90.root',
] )




































