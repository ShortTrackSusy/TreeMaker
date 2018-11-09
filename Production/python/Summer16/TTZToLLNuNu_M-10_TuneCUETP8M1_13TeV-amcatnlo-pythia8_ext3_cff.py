import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/024C1DAE-6303-E711-B126-C45444922C46.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/087B2BB0-8703-E711-80B3-008CFA11131C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/0A17F603-2A04-E711-8B89-0CC47A7FC7AE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/0A494BEB-A302-E711-920F-02163E01A663.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/0A6F24C1-6903-E711-A7EA-02163E012D2E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/0C66FF0F-6F03-E711-B6B9-FA163E627D84.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/127914D9-8D01-E711-BFEA-0025905C42FE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/142E340A-4D03-E711-9899-02163E019BC5.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/1491A3BE-BD01-E711-BA43-02163E0139CB.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/14AD52A4-7B01-E711-99F4-0CC47A5FC679.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/16EE328E-4403-E711-B593-FA163E472DB1.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/18066ACD-8D01-E711-A502-008CFA1980B8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/1A0DD089-6A03-E711-8466-FA163E459F1A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/1A7D2DA3-6A03-E711-8055-FA163E18141A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/1AF1BF9A-6203-E711-9323-02163E0144CC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/20501930-B101-E711-9D85-F4E9D497BBE0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/226ED30F-8E01-E711-9522-0025905C53A6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/22D7CA1F-1406-E711-9F18-842B2B76653D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/22E7B284-7501-E711-BAC7-0CC47A5FC67D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/246C3321-CF03-E711-A27A-3417EBE47FE5.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/24B9699A-5102-E711-9860-549F35AD8B7B.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/260C77DA-6C03-E711-A133-FA163E40806D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/26A87CDA-1F04-E711-8D0D-002590D9D976.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/28079609-3A04-E711-B516-0025907DCAA6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/2A8746E2-1306-E711-BE5F-E41D2D08DDF0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/2AEB167C-6B03-E711-A558-02163E00B091.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/2CB575FE-5502-E711-8CB9-0025904C7A54.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/2E0A8FC5-8D01-E711-B115-A0369FC5F804.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/2E2C6E98-5803-E711-95C5-FA163E05B485.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/3053C1C4-9301-E711-9238-3417EBE64774.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/30632ABE-B201-E711-85D1-02163E019CCC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/30D8A4E2-A301-E711-9F54-000AE488BCD7.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/3259F684-7C02-E711-A970-0CC47A7EEDB0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/32D5BA2C-AE01-E711-BB7D-842B2B7669E2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/36B82B86-0602-E711-862A-20CF3019DF0C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/38BE507C-1F02-E711-8531-002590E7E010.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/38C335B8-9F01-E711-9369-7845C4FC397A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/3A271878-2604-E711-8C06-0CC47A7FC7AE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/3C80036C-6503-E711-ADF3-FA163E9AD52A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/3E2B7C4A-6B03-E711-9B38-002590494D18.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/4060009C-8103-E711-9E3D-0025905D1C56.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/40E20DE4-CB04-E711-B0F7-008CFAFC0080.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/4273578E-4B03-E711-9395-FA163E602758.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/42B7E901-4704-E711-91EF-70106F4A9384.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/445E3C70-F603-E711-8FEF-14DDA924324B.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/44C979E5-4D02-E711-BE29-047D7B10618E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/48DFFB06-6C03-E711-85E9-02163E017612.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/4C96FDA2-3603-E711-96CB-0025905B8592.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/4CFF1CD7-9901-E711-A122-F4E9D497BBE0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/5007F795-5C03-E711-8A13-02163E0135F3.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/504D6DF1-7202-E711-BB0E-008CFAF5543C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/5407A7F7-D302-E711-9844-0CC47A4DECCE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/565A7C62-5302-E711-9D77-24BE05C6E7C1.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/56D571FB-9F01-E711-98FC-008CFAF554E6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/58044768-6C03-E711-B43C-FA163E824933.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/5834174D-B101-E711-8CF5-0CC47A00A832.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/5A3F7DCF-B304-E711-A16D-C81F66C8BA4C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/5C40B559-5403-E711-8FF1-02163E01A35C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/5C422D6B-9C02-E711-86F6-002590E3A224.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/5EAB20CE-1A04-E711-8E08-002590E7DE70.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/602A4832-2C04-E711-BA4B-002590DB92A8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/6611247F-1703-E711-BC9C-002481DE4CC2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/66D26047-3204-E711-BD8E-7845C4FC3647.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/66E440DE-5903-E711-A8A7-FA163E2A1984.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/682582D7-4A03-E711-808E-FA163EECA31F.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/6A877E74-6B03-E711-A9C8-02163E011475.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/6C41095F-2B03-E711-87E7-002590FD583A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/6CC08003-5E03-E711-8B98-FA163E8239E7.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/70ED2A72-C001-E711-BBF9-02163E01A5B3.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/72BF14D5-A401-E711-B021-F4E9D497BBE0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/766A70CD-8D01-E711-9E3B-008CFA0A58F8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/76C0199D-8701-E711-86B0-008CFA1982C0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/787794E6-6703-E711-B965-FA163E067CF3.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/78EE7416-B001-E711-AAF8-848F69FD29B2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/7AC53050-CD01-E711-A654-02163E01A231.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/7C916B71-EB04-E711-B3B3-FA163E903195.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/7CE815DF-9301-E711-8983-0025905C2CD2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/7E91E6BC-C601-E711-9DF8-02163E0125A7.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/805FED8F-8101-E711-AB1D-0CC47A5FC495.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/86AE14DF-0D04-E711-90AE-1CC1DE782F02.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/8847B1EF-AE01-E711-807A-008CFAF75602.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/88560E24-7C02-E711-B305-008CFAF75602.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/8AD2C591-3B04-E711-892F-02163E00AE49.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/8C4C225A-B304-E711-87CF-0CC47A745250.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/8E0691C2-4E03-E711-9685-FA163E459F1A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/90E312AC-8D01-E711-AACA-00266CFFCD14.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/921FD8FB-6A03-E711-9415-FA163E0614A7.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/94A37018-BB04-E711-A3B3-008CFA0A56F0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/967E8788-7202-E711-8476-002590D9DA9C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/96DA679D-8101-E711-A848-001E4F1BC725.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/980135D8-3F03-E711-838A-002590494DC0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/984AEEFB-5602-E711-9151-B083FECFC6ED.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/9899400B-3B04-E711-A705-001E67457A5D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/9A0C5A92-7202-E711-BA66-20CF3027A5C5.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/9CD82400-CE04-E711-B368-1CB72C1B2D84.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/9E05C753-B304-E711-B579-0025905C42A2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/9E5A10C0-9102-E711-A4F5-848F69FD4565.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/A01D5D6C-B304-E711-9C5E-001E6750507D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/A0A86BCE-8D01-E711-80DB-848F69FD29B2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/A0F2C20D-EE01-E711-9752-28924A33AFC2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/A248E14E-1406-E711-BDF1-0025904C7DFA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/A4BCCD1C-A404-E711-A615-6CC2173BBA30.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/A4BD487C-2D04-E711-B962-047D7B881D10.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/A8D8E92F-3D03-E711-AD99-FA163E510E95.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/AA1BB408-5602-E711-92B0-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/AAA49CD1-9901-E711-9BF0-3417EBE527EF.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/AE3EF337-1E04-E711-8D2C-FA163ED6DEFE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/AE8257AB-C103-E711-BC21-842B2B75FDA9.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/B203E6A2-2E04-E711-98AA-02163E01A30D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/B21FA481-4F02-E711-90AE-24BE05C44BB1.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/B2320AB3-3F03-E711-AF3D-FA163E436FDA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/B2474958-B304-E711-8EF4-00259073E382.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/BABE7AC3-9F01-E711-AF83-7CD30AC030C4.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/BE3748DF-9301-E711-B38D-0025905C53D0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/BE88B858-4803-E711-8B99-FA163E259F0D.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/C05C8487-BA01-E711-82BC-02163E0145A3.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/C0A9E729-2003-E711-936E-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/C42D7FA1-B602-E711-BBEE-0025904C637A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/C4659505-6902-E711-B173-0025905C4264.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/C4BE3FCA-8D01-E711-85C8-0CC47A706CD6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/C6C5689F-D304-E711-821B-28924A35059A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/C8423BA6-8D01-E711-AB8D-6CC21739DBD0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/C8C53EC5-6F01-E711-9A07-0CC47A5FC2A1.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/CC0FC6F5-2F04-E711-A753-E41D2D08DD70.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/CC85259A-9402-E711-B7B9-001EC9ADC046.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/D486FDA4-6603-E711-8F99-001E6757A200.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/D6435BB3-C401-E711-A825-02163E01A449.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/D678424E-9402-E711-8464-0025905C43EC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/D6C55CA9-6302-E711-A166-0026B93F4C1B.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/D867380A-4B03-E711-B6FB-02163E017618.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/D8B2717D-4502-E711-9178-002590200A94.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/DAC0C12B-5E03-E711-9DB0-00145E5522D0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/E23A7576-CF02-E711-881D-001EC94BF71A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/E801BA85-8701-E711-B21A-14187763663C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/E87FEAF3-2703-E711-B420-001E67E6F7F6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/EA1BCB65-D901-E711-A5DC-02163E01435F.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/EC719B40-AB04-E711-AD4D-B083FECF83AB.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/EC9AA3A7-7501-E711-A30C-90B11CBCFFF7.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/EE4050C8-FF01-E711-90DC-D8D385AF889C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/F06DB366-B304-E711-A63D-002481DE4818.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/F410CEE8-8502-E711-A7EE-C4346BC8C638.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/F4EF69D5-8D01-E711-A175-002590D4FBB6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/F833EE97-4803-E711-93D6-FA163EE124FD.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/F83D66D2-5002-E711-BDD0-441EA171A998.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/FC14D0FA-9301-E711-8416-00266CFFCA1C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/FC4982D1-9901-E711-AB99-3417EBE64BB5.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/FC756DF4-DE04-E711-B8BD-D4AE526A10E8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/FCE7FB6C-B901-E711-AF0E-DEDBE4AC1313.root',
       '/store/mc/RunIISummer16MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/110000/FCFDCA9A-EB02-E711-857A-002590E7D5A6.root',
] )
