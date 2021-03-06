import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/564D9B67-7EA7-E611-BFC1-D4AE527EE013.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/46AF083A-83A7-E611-B465-B083FED04D68.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DC1E16F1-86A7-E611-B094-141877411936.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/662ACF8A-8FA7-E611-A0AB-1866DAEA7F94.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/90762A1B-97A7-E611-8E19-1418774120C3.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CEAA67C8-9EA7-E611-A4F9-842B2B42B2B1.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/30D8FD1E-A0A7-E611-B2D2-1866DAEA6D0C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4A8B1106-A6A7-E611-9234-842B2B1814F5.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0405DE96-ABA7-E611-B779-B083FED406AD.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/123E59BD-AEA7-E611-8C49-1866DAEB3628.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/56384F0D-B2A7-E611-9F68-141877411936.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2E3C643F-B7A7-E611-A097-1866DAEA8178.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/96C2A399-BBA7-E611-8F26-B083FED14CE0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3C1544F2-BFA7-E611-9C92-782BCB537DBB.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/68374D62-C1A7-E611-8C94-B083FECF837B.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/74F0209E-C4A7-E611-BDE1-14187741136B.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/18FA9795-C6A7-E611-BE14-90B11C0BB9CF.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5E8B74C5-C9A7-E611-9D63-141877410340.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8AE02C8E-CCA7-E611-8ABB-14187741208F.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E43C441C-D0A7-E611-BD80-1866DAEA79D0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/66CC168D-D0A7-E611-B243-141877411C7F.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D8227232-D0A7-E611-89F9-549F3525E81C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8C15962F-D6A7-E611-9EA3-1866DAEA79C8.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BCF48E96-DAA7-E611-ADAD-90B11C0BCD75.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5C4DD2E6-DFA7-E611-AF25-842B2B181725.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6E953887-E3A7-E611-BAA1-1418774124DE.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A46BCBAD-E6A7-E611-A519-A4BADB1E6F7A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/24409768-EDA7-E611-86FB-90B11C0BCBC2.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4626C701-F4A7-E611-81F9-B083FED18BA0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0E45D174-F9A7-E611-AA68-549F3525B154.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A8BD8E3E-05A8-E611-9992-1866DAEA7E28.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D62A5CF3-0FA8-E611-B823-549F3525C0BC.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E8D81694-1CA8-E611-BC30-549F3525CD78.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2C9EBBCD-25A8-E611-A1EE-549F3525DB98.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F41CED3E-2DA8-E611-89AA-141877411367.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A0B7B45F-35A8-E611-BA98-1866DAEB296C.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/22D35C84-43A8-E611-BF13-B083FED42488.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/344C2B56-4AA8-E611-984A-1418774117C7.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4EE29787-51A8-E611-84CF-0026B9457805.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/36B8058B-59A8-E611-A282-B083FED14CE0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/76AF0C04-70A8-E611-956B-141877410340.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2C0A00CC-56AA-E611-BE95-782BCB539A80.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/94E0AD26-60AA-E611-8368-782BCB53A09D.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4CBB6C9E-69AA-E611-B45F-001C23C0F203.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9CA34A6A-6EAA-E611-AE60-B083FED3F4E3.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/02C67C52-76AA-E611-9E87-842B2B172901.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9C304BB5-7CAA-E611-97DF-1866DAEA6CC4.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CE7312FF-96AA-E611-896C-782BCB206037.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4A759D37-B0AA-E611-893B-549F3525C0BC.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/881E3846-BAAB-E611-9D66-1866DAEA6CF0.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/702CE9F9-8AAD-E611-9D0C-B083FED3F4E3.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AE1DC0FA-92AD-E611-986D-C81F66B7EBF5.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FC43ED2B-98AD-E611-937D-1866DAEA7E64.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/20F4DC04-9CAD-E611-95DF-A4BADB1C0EF3.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F405B5E9-9EAD-E611-8E0C-141877410ACD.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D803DB5A-A3AD-E611-897C-782BCB20E908.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F6530960-A7AD-E611-82FC-001C23C105F2.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FEFA16E9-ACAD-E611-8FA7-D4AE527EDE00.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9EB3CAA2-AFAD-E611-9B31-1418774121A1.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4CB4D7AA-B4AD-E611-9FE5-D4AE526DF3BB.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CEC1A4F9-EFAD-E611-AA4C-549F3525CD78.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0AC06BF5-98AD-E611-B128-0CC47A6C138A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C80CA01C-A1AD-E611-8282-002590E3A222.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9A851553-A5AD-E611-8601-002590CB0B5A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/16ED27D3-A7AD-E611-804F-0CC47A6C1058.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/187A877C-ABAD-E611-953A-0025901D0C4E.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C00F3028-B0AD-E611-B45D-90B11C2CC76A.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/946A2570-CBAD-E611-AB17-0CC47A13D0F2.root',
'/store/mc/RunIISummer16DR80Premix/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D695D5AF-F0AD-E611-B688-0025900E3502.root',
] )




































