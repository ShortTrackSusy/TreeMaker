import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/026EE3D8-F7CA-E611-822D-24BE05C64601.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D0EF6BE2-F7CA-E611-B526-A0369F310374.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DE2436DF-F7CA-E611-ABC9-E0071B7AF7C0.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1A47C4DD-F8CA-E611-8704-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E4357312-F8CA-E611-9CF5-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EABDBD11-F8CA-E611-9FF2-4C79BA260AFD.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/12C07729-F7CA-E611-A6F6-A0369F30FFD2.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5E2188F9-FACA-E611-B680-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/66A8BD36-F9CA-E611-B3C7-A0369F3102F6.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8A92EE8D-F9CA-E611-907E-B8CA3A70BAC8.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FE7BFB75-FCCA-E611-B0A5-E0071B749CA0.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4EAAF372-FCCA-E611-B04D-24BE05BD4F61.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AE9F0273-FCCA-E611-9617-24BE05CEDCF1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0CCED125-FDCA-E611-9F65-24BE05C63791.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4AADFBF9-FACA-E611-866C-A0369F30FFD2.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/26397571-FCCA-E611-88F7-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/006212F6-FACA-E611-9B69-B8CA3A709028.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8040E82D-FDCA-E611-B767-24BE05C656A1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EA4D2033-FDCA-E611-AABD-E0071B7AC7C0.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/22967577-FCCA-E611-B59E-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6429AE59-FDCA-E611-9265-24BE05C46B11.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BC37F179-FCCA-E611-A192-2C4138EBD370.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8A3C8551-FFCA-E611-A047-24BE05CEDCF1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/740B5E81-0BCB-E611-B467-E0071B7AC750.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/14B499E9-0ACB-E611-8932-A0369F3102B6.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FABC1A99-09CB-E611-846C-B8CA3A709648.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1635CD17-0DCB-E611-8308-5065F3820351.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A4671980-0BCB-E611-92DF-E0071B7A8560.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2E8A5829-0DCB-E611-9B33-24BE05C6C7F1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1C5A350C-0DCB-E611-BB9F-5065F3815241.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0CEC6432-0DCB-E611-A62A-24BE05C63791.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DCD7BEB2-0DCB-E611-B658-24BE05CEEDB1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DE6E6980-0BCB-E611-B313-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/821FBBF0-0DCB-E611-A2D0-24BE05C6D711.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/426FD4C1-0ECB-E611-A9FB-24BE05C618F1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B46420EB-0ECB-E611-B1BC-E0071B7AC750.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1AAAA09B-0FCB-E611-9D49-24BE05CEBD61.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6A27E39A-0FCB-E611-9264-5065F3812201.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8E479199-0FCB-E611-8A74-5065F382C251.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/529728BD-0ECB-E611-9D89-B8CA3A70A410.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2E0F7A99-0FCB-E611-96A7-5065F3810301.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/12F148A0-0FCB-E611-84F5-E0071B7A5540.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E6C77AED-0DCB-E611-B8F1-A0369F3102B6.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/043C5705-0FCB-E611-BD2F-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5846B89A-0FCB-E611-AB81-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/66F05CEC-10CB-E611-ABEF-24BE05CE5D21.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D8413067-FFCA-E611-979A-E0071B749CA0.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B02E8462-FFCA-E611-8E43-24BE05BD4F61.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4E504A31-00CB-E611-9BFE-24BE05C63791.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AE290553-FECA-E611-B687-A0369F3102B6.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5454F550-FECA-E611-9956-A0000620FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3C332E36-00CB-E611-9BC5-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5C906148-01CB-E611-A4E3-24BE05C3B8B1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8223B0B0-FFCA-E611-B3D9-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/66500068-00CB-E611-9E98-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F033DB33-00CB-E611-BE70-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4CF13439-00CB-E611-9F34-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/165A7E5F-03CB-E611-A322-24BE05C4D801.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/18EEE322-03CB-E611-9E0C-5065F38172A1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2EC32F5F-03CB-E611-BB91-24BE05CEADA1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F410305F-03CB-E611-8162-24BE05CEEDB1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2EF5E048-04CB-E611-BDAB-5065F3818261.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B4792FD0-05CB-E611-8F67-24BE05C6D711.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/80CFCD43-04CB-E611-89C2-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/00FC3250-04CB-E611-9C62-A0369F3102B6.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E251CC4C-04CB-E611-849A-A0369F30FFD2.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/343C60D0-05CB-E611-B4F5-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AA48DECE-06CB-E611-AE37-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6AA6D899-0ACB-E611-B477-24BE05CEEDB1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/22AB18C6-0ECB-E611-B883-B8CA3A709648.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/78ECD00C-0FCB-E611-ADCB-A0369F3102B6.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7CF3ADA1-0FCB-E611-BA1F-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6EB96F9B-0FCB-E611-9632-B8CA3A70A5E8.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4A046DF3-10CB-E611-9830-4C79BA1812D3.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/ACAF2E6C-0FCB-E611-ABEF-A0369F30FFD2.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FC62E2EA-10CB-E611-BFFC-A0000620FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B4E1F2D9-11CB-E611-BA73-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BEF669DF-11CB-E611-943D-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F20724C7-11CB-E611-9D06-A0000620FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8C57E8D7-11CB-E611-B89A-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/44C961F9-10CB-E611-B1D9-4C79BA3201DF.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9673AC73-13CB-E611-A9D1-24BE05C38CA1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1C51267D-13CB-E611-836C-E0071B749C80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AAAADE32-13CB-E611-B61A-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/66534F93-14CB-E611-8FCB-B8CA3A70A5E8.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4E2021BE-12CB-E611-93E5-B8CA3A70A410.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/646EF11A-13CB-E611-B884-A0369F3102B6.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7C5C4EB7-13CB-E611-9AED-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B685E4D6-13CB-E611-913E-B8CA3A70BAC8.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/249BD585-13CB-E611-ABD4-A0369F30FFD2.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/329AAF67-FACA-E611-B3DD-E0071B745DC0.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9ECB6306-37CB-E611-92AC-A0369F3102F6.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F4900D19-E7CA-E611-8626-5065F37DD491.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/28D9C0FF-E9CA-E611-88A1-A0369F30FFD2.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BA6B03FB-EBCA-E611-AAAD-5065F3812271.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C0CBDABD-F0CA-E611-8FBB-5065F381E211.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E6E2A04B-F1CA-E611-8899-5065F3812271.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D285732E-EECA-E611-8FDC-A0369F3016EC.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AEE0958A-F2CA-E611-AF7F-24BE05C488E1.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/14C5DA21-F4CA-E611-A8A1-A0000620FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A25E65EC-D6CA-E611-A20E-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7621F34A-D6CA-E611-98B7-E0071B745DC0.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/980111BC-EACA-E611-841F-5065F37DD491.root',
] )






