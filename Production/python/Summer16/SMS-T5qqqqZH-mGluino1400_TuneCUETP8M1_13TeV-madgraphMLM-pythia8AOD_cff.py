import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/FEE8F942-FDF5-E611-A9D4-1CC1DE1CF69A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D85DCC6C-02F6-E611-A695-5C260AFFFB57.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BAD7019C-1EF6-E611-9AE2-A0369F63681A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B6D5FB3C-47F7-E611-9291-0CC47A4D765E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/30A26ED7-C1F6-E611-B688-FA163E4B408A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/FCD5B876-3EF5-E611-BDAA-44A842CF061A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/58211167-44F5-E611-887F-44A842CF05CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/40F12862-0FF6-E611-8796-001CC4A68B8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/669E88C2-40F5-E611-850D-FA163E5EB566.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/1AC014CA-40F5-E611-9810-0CC47A04486C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/868E35BF-40F5-E611-8CC6-FA163E550F34.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/0C54E1B3-40F5-E611-B4AB-2C600CAFEFA8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3067C739-39F5-E611-97F7-FA163E62DB22.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/20A78507-41F5-E611-AE48-001E67C7B165.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/48F08BB3-40F5-E611-A02B-FA163EA08442.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/64803ED0-C3F6-E611-990D-FA163E86B60D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/326619C6-C1F6-E611-94DD-FA163E7F5A2A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9EC3F03E-0DF6-E611-9A5A-009C02AAB554.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/44209BCD-08F6-E611-8011-008CFAFBFCA8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3E447971-18F6-E611-9179-D8D385AF8AEE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D2EDA1FA-38F5-E611-A90B-0CC47A4D769C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9C16C9F9-38F5-E611-95E4-0CC47A78A33E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/24D00816-3CF5-E611-B072-0CC47A4D761A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/5A78664A-3AF5-E611-A328-0025905A60F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/50E43680-3BF5-E611-814F-0CC47A7C35D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E40C65F0-3AF5-E611-9BE4-0025905A48BC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/804B2906-40F5-E611-A92A-0CC47A7C340C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7E33515F-3DF5-E611-93E7-0CC47A4D76A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9006FCFB-3DF5-E611-9977-0CC47A4C8E64.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F670E578-3EF5-E611-89F2-0CC47A7C345C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B4168AFD-3DF5-E611-B1EA-0025905B8562.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9E26743B-3FF5-E611-BC29-0CC47A4C8F12.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6E8D1280-3EF5-E611-B0EB-0025905A60F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6C3C6C3C-3FF5-E611-865C-0025905A60F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/62A07C0D-40F5-E611-9E63-0025905A48BC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/B0D69071-43F5-E611-A4BD-0CC47A7C3612.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/208E1683-3EF5-E611-B72D-0025905A6092.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/48401582-43F5-E611-9FFD-0CC47A78A436.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/5CCC7E6D-44F5-E611-9F99-0CC47A4C8F30.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3A3D6570-43F5-E611-9AE9-0CC47A74525A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/DE391178-44F5-E611-B82C-0CC47A7C345C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C61567F4-44F5-E611-B2A6-0CC47A4C8F10.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A47354EE-44F5-E611-AF32-0CC47A4D76AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7C026A86-44F5-E611-83FD-0CC47A78A45A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CA82A2D2-46F5-E611-9249-0025905A60D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2A8001A8-46F5-E611-9C77-0025905A6076.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/EA8241A7-44F5-E611-A62E-0025905A6084.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/54329C33-44F5-E611-8A26-0025905B8562.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/48E59EB6-4DF6-E611-83FD-0025905B8566.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/506300AC-4DF6-E611-B2F2-0025905B8594.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D2454902-3CF5-E611-9884-0025905C2CD0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7A784A6A-3EF5-E611-BC6B-0025904C6376.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C0A06C99-3DF5-E611-ACC9-0025905C5488.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F88CF275-3EF5-E611-B763-0025904CF93C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/0E5A0BD2-08F6-E611-BBC5-0025905C3E36.root',
] )




































