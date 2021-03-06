import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/344FDCE3-718C-E911-8BEC-008CFAC9429C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/B6AAA3BF-2689-E911-B763-0242AC1C0500.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/96C30086-ED87-E911-86AB-001F2908AED8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/A87F16DB-FA87-E911-A14E-44A842CFC97E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/C42DCFE9-FA87-E911-9642-B499BAAC0626.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/7A8D382C-1688-E911-B725-6C3BE5B541F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/46064D69-1F89-E911-8106-6C3BE5B564A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/1AB4F7CB-CE8B-E911-9EBD-0CC47AD98D00.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/245CEF18-F68B-E911-B746-0025907277FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/B06C2BE0-FA87-E911-8A05-A0369FF8841A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/6E0C0A77-FF87-E911-9BEC-A0369FF88396.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/E8B407FC-D188-E911-8138-A0369FC51BB4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/A465F4EC-718A-E911-915A-B026283D9360.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/76B575DF-3F8B-E911-B5AA-B026283D9360.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/F21C1209-4B8B-E911-9B79-BC305B390A8D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/B0E6A4AA-E089-E911-A3A3-001E6779281C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/F6E9D320-4B8B-E911-93E3-A4BF01158888.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/9AFA4FD3-5089-E911-92A8-0025905C3DD8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/86572F7F-CF8B-E911-9A9C-00266CF94D50.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/32D6198D-FF88-E911-9BF9-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/CA741E14-7A8D-E911-B5A0-00259090848A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/92243EF1-8189-E911-B8DE-0025902D14EA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/10CBE82E-7B88-E911-8FB7-AC1F6BAC7C16.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/CE853D4D-0C89-E911-9E11-0CC47A4C8EC6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/94498D57-7488-E911-96E8-B083FED024B1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/80CD759D-2A89-E911-9F23-1866DAEA79D4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/BA12BB7C-FF88-E911-BFB5-008CFAC91874.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/4E99EAAB-D589-E911-A6E2-A0369FE2C21E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/EE03B2F1-9188-E911-9DC5-008CFAF75512.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/6E6E5207-6A88-E911-AE79-0CC47AC08BF8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/A49FC780-4089-E911-84CD-AC1F6B0F3A26.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/EE0A82FA-8E88-E911-8C64-A4BF0128811C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/5637F73A-9E89-E911-8F97-3417EBE705CD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/18890F1F-1189-E911-AE3F-24BE05C4D8C1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/E6601730-0C89-E911-9856-0CC47AFC3C76.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/3C7E6EFA-B388-E911-ADAC-FA163EFD160B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/B2B6FE10-128A-E911-931A-002590DC03C6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/F6B54559-E48A-E911-84FF-AC1F6BB1780A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/2A8CC008-508B-E911-8810-3417EBE649FF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/6081B60D-D48B-E911-85C5-405CFDE57581.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/0ACB6874-E18A-E911-A1B1-90E2BACBAD58.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/80EAE910-E88A-E911-B194-68CC6EA5BE3A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/06E252CC-5E8B-E911-8EC5-0CC47A5FC285.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/E8EEA330-DD8B-E911-ABBC-6CC2173C3DD0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/8E5A6791-BB8B-E911-9F88-A0369FE2C158.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/82FCBBCF-5F8C-E911-8521-B8AC6F16E24B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/5664048F-3B8B-E911-99AC-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/582593DA-D48B-E911-AF2B-0CC47AF97126.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/B21220E9-4588-E911-8116-001E67DDC4AC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/AAF52467-498B-E911-B9D9-FA163EE5AD6C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/92FDD60D-5591-E911-A765-20040FE9C898.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/FCFAB4AD-CC8E-E911-8A2A-001CC4A68B9C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/30000/E675E6D6-2490-E911-BB64-00266CFFCD14.root',
] )















