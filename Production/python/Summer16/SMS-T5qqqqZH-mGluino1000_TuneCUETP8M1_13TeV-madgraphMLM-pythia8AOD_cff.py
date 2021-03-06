import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/12CDDBDC-43F5-E611-B3AD-0CC47A4C8E98.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7C640F96-46F5-E611-82C2-0CC47A4C8F1C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/10559586-46F5-E611-96DC-0CC47A4D7658.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/68C1D147-48F5-E611-BC77-0CC47A4C8EB6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AAED5B45-48F5-E611-83A0-0CC47A7C35B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3408242A-47F5-E611-9E4A-0CC47A4D7664.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/427F4B4B-47F5-E611-8E55-0CC47A78A478.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/024C8130-4AF5-E611-A9CA-0CC47A4D7670.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BA6F44FA-4AF5-E611-9968-0CC47A7C34E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D4B89585-4CF5-E611-8453-0CC47A74525A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B453C283-4CF5-E611-B4B2-0CC47A4D7646.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A0A9EA87-4CF5-E611-AF23-0025905B85C6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B8107440-4AF5-E611-A4D1-0025905B85D6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A096CCFB-4AF5-E611-8DF2-0025905A60BC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BA155587-4DF5-E611-B492-0025905A60DE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AED75A8A-4DF5-E611-8417-0025905B85AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/447EE7D2-4FF5-E611-9F1A-0025905B8610.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CC09CE43-5DF5-E611-BCD4-0CC47A7C360E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/0278EAC3-5DF5-E611-8FFE-0CC47A4C8E2E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/447C22A0-53F5-E611-8E23-0CC47A78A3E8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/9A700B90-53F5-E611-8BEA-0CC47A4C8E22.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/D29495E2-65F5-E611-829D-0CC47A7C351E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/CC6BDF71-75F5-E611-AAE7-0CC47A78A42C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/7C4A0F72-75F5-E611-A09A-0CC47A4C8E22.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/B60F0F78-75F5-E611-98B9-0CC47A4D7692.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/B2B75B73-75F5-E611-BD4C-0CC47A4C8ECE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/0651E583-75F5-E611-BD31-0025905B85AE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/26421575-75F5-E611-88F2-0025905B85B6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/1492607D-75F5-E611-99C2-0025905B85D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/44FF2A75-75F5-E611-995D-0025905A613C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/742A7B85-7DF5-E611-BF51-0CC47A7C361E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/9E63FD95-7DF5-E611-9E96-0CC47A4D7674.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C868E176-75F5-E611-BD16-0025905B85D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/404D637C-7DF5-E611-8B00-0CC47A4C8ECE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/18291AD0-7DF5-E611-9311-0025905B85B6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/249938CC-7DF5-E611-AADB-0025905A613C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/6EB43BFF-7DF5-E611-B536-0CC47A4D767A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C2E28F8C-7EF5-E611-8A05-0CC47A78A436.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/46DC6EEF-7DF5-E611-9342-0025905B85D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C40BE908-7EF5-E611-8D35-0025905B85AE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/A2F79C14-44F6-E611-84F8-0CC47A4D764C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/EA08342E-44F6-E611-9C8A-0CC47A4D767E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AAA54400-F1F5-E611-AC8E-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/680C99EF-37F6-E611-8822-0025905C53A4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/487C4875-FEF5-E611-89F7-B499BAAC0A22.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/0A9A675A-C9F6-E611-9FD3-6C3BE5B5F210.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/28F2FDA4-40F6-E611-865A-3417EBE465FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/224D9DC3-19F6-E611-A76B-00259029ED64.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C4D79B90-12F6-E611-A48F-002481CFE7F2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/CEB58A16-6AFB-E611-8C5A-02163E00B205.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/B6F20739-69FB-E611-9B3C-FA163E6A48AF.root',
] )




































