import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7AEE8BE1-86BA-E611-B8A2-0CC47AC08908.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7C99FE80-8BBA-E611-A5F7-002590DE6E3A.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8C117DB8-8EBA-E611-BACA-002590DE6E3A.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EA5A8673-96BA-E611-9FF7-0025904C7F72.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/663523A6-98BA-E611-9A3B-002590DE6E3A.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7ED6582A-99BA-E611-B132-002590DE6C96.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0E5B3911-9ABA-E611-A653-0025904C7F72.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C4F9F986-9BBA-E611-9CFD-002590DE6C48.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/720067D7-9CBA-E611-8692-0025904C7C24.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/48E16FF8-9DBA-E611-8B26-002590DE6C48.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D619FEDA-A2BA-E611-9139-0025904C7A5C.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1A9E5DB4-A1BA-E611-9C60-0025904C7FBE.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/16070487-A5BA-E611-BF8E-0025904C7A5E.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6A35D9E2-88BA-E611-8433-0090FAA58754.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F4D8257C-89BA-E611-ADC4-0090FAA579F0.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4CC0AE47-87BA-E611-AD8A-00259074AEAE.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/007A5E04-8ABA-E611-B0A1-0090FAA58754.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CEF0D172-8BBA-E611-8A41-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/62F0CFE8-88BA-E611-AD66-00259073E3D4.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3E169C82-8ABA-E611-BF0D-002590747E28.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C0BD998B-8CBA-E611-8E68-0090FAA58754.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4601100E-8EBA-E611-9170-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2B6527A-8BBA-E611-B798-00259074AE9A.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A669ED14-8CBA-E611-B6E0-00259073E4EA.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/94CF9D7A-8BBA-E611-B1DC-00259074AEAE.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2A1CBB9A-8EBA-E611-AE0E-0090FAA576C0.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C4F88429-8DBA-E611-868F-00259073E442.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9A1B3CA1-8DBA-E611-AF62-00259073E4E4.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B491F812-8EBA-E611-863D-00259073E4B4.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2ECEA832-8FBA-E611-865F-00259073E3D4.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4096855B-91BA-E611-8550-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4E6C4095-90BA-E611-BFC7-0090FAA58754.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/98D138B5-91BA-E611-B5DE-0090FAA58754.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/44059760-8FBA-E611-96A2-002590747E28.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/863A92A7-8FBA-E611-BDA2-00259073E3DA.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A687B930-90BA-E611-BD96-00259073E4E2.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AC6C9FA0-90BA-E611-9823-00259073E406.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0A583C3B-92BA-E611-B1FF-00259073E34E.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DE131F88-91BA-E611-A989-00259074AE9A.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/04C3D0F3-94BA-E611-B2C4-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/36BCFDCE-93BA-E611-BD9A-00259073E452.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/023F5CBB-95BA-E611-963B-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EA7C5A26-93BA-E611-B6BC-00259073E4E4.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E8D3E049-94BA-E611-8911-00259073E4B4.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/36DD908F-97BA-E611-926B-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/14776153-95BA-E611-8AA9-00259074AEAE.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3E6462C2-95BA-E611-9AAF-00259074AE38.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2AF382F-98BA-E611-B556-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5C39F3E2-96BA-E611-9235-00259073E406.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/80FE214E-96BA-E611-9B5E-00259073E3DA.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D29333B2-98BA-E611-9CC7-20CF3019DEED.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/60B56164-9ABA-E611-AEEF-00259074AEAE.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/94C68582-9ABA-E611-B68A-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/30ACAF5E-9ABA-E611-BAE3-0090FAA56994.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/00AE4E67-99BA-E611-9BB7-00259073E3DA.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3CF1BAF6-9BBA-E611-8AD7-0090FAA58D24.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0465CDF1-9DBA-E611-AFF0-0090FAA57780.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6C941F6F-9BBA-E611-A7AC-00259074AEAE.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/40D1E676-9DBA-E611-BD78-002590747D90.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/ACD469F7-9DBA-E611-B341-00259073E4CC.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/94342E8D-9CBA-E611-9A58-00259073E406.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9A0D3653-9FBA-E611-8BAE-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DA3BB977-9DBA-E611-A944-00259073E524.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/82462A3D-A0BA-E611-A4D7-0090FAA58D24.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6088E1CD-A1BA-E611-B9F8-0090FAA582E4.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5E60CBDE-9EBA-E611-807A-00259074AE7A.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/34A3053E-A1BA-E611-8197-0090FAA56994.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3E56BD52-9FBA-E611-A659-00259073E44E.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DA6806CC-A1BA-E611-9D39-0090FAA579F0.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F654DA40-A1BA-E611-8E79-0090FAA576C0.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/449B4EDA-9FBA-E611-B81E-00259073E3DA.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0AB4239F-A4BA-E611-B2BB-0090FAA58D24.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CE66C8D1-A1BA-E611-AB75-00259073E442.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/624AF1D1-A1BA-E611-A022-00259073E34E.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FC394188-A3BA-E611-B815-0090FAA59864.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2C3F6545-A1BA-E611-BCEC-00259073E3DA.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CE37F041-A2BA-E611-ACA6-00259073E452.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/96140927-A5BA-E611-B554-00259074AE7A.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/96EC51D6-A2BA-E611-90C5-00259074AEAE.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/82948AD8-A6BA-E611-BEE7-0090FAA58D24.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/343B0219-A5BA-E611-8255-0090FAA58274.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/08897C90-A5BA-E611-BCF5-00259073E44E.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DE383030-A4BA-E611-B3B6-0025907B4FC4.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5EDADAB4-A3BA-E611-839C-00259073E406.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C6EBF419-A6BA-E611-B5CC-0CC47A4DECD6.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2AC02E86-A4BA-E611-AB3F-00259073E4B4.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B4BF93FD-A7BA-E611-8031-00259073E452.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7474EF93-A5BA-E611-8DBA-002590747DDC.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CE372756-A7BA-E611-B9CA-00259074AE40.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7E7470EE-A6BA-E611-9913-00259073E4E2.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B0E0AF27-A9BA-E611-AB9B-00259074AEAE.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A0170C39-ABBA-E611-B9D4-002590747DDC.root',
'/store/mc/RunIISummer16DR80Premix/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/623E9184-B0BA-E611-855A-00259073E44E.root',
] )




































