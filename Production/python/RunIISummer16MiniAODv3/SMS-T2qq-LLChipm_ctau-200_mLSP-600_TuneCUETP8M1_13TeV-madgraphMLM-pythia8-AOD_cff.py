import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/DC1D6DEF-5388-E911-9A83-001E675A659A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/C00BB131-0589-E911-B9E9-0025901AA5AE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/A2712DD2-2789-E911-B3D2-EC0D9A0B3350.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/AC6765F8-2C8A-E911-B0FA-0CC47A5FC2A5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/B8D06E5E-FF87-E911-97DC-008CFA56D770.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/6C05F370-CF88-E911-9C0D-A0369F7FC524.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/A6209A2F-518D-E911-860C-0242AC1C0501.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/00FD8E6E-AB8C-E911-9A16-A0369F63681A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/6A4B843D-BF88-E911-838D-001E67E59BE3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/263A68A8-DE88-E911-AEE6-1866DA87931C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/8A5E2B35-D28A-E911-A4A1-A0369FF8852A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/5C5893F9-E088-E911-AB73-3417EBE706C6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/4EDFA3F4-9388-E911-BA93-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/DAF5C732-148B-E911-9FB9-AC1F6BAC807A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/7A246E7C-098C-E911-8C38-141877638F39.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/3036D519-0B8C-E911-B840-246E96D14B5C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/96EE721E-0E8C-E911-A84F-14187764197C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/08A521C6-A28C-E911-B5FD-0CC47AFC3C80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/D6D27DFF-8D8D-E911-B7CA-141877642ECF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/C2D8821A-E088-E911-96E7-44A842B4B3F1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/4C3CD8E8-7488-E911-8B24-0242AC1C0503.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F4EAE50A-DF88-E911-A16E-44A842CFC9F3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/08FA1586-3C8A-E911-958E-484D7E8DF078.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/50A8D478-4188-E911-A4EB-B026283D86C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/5076618F-5A8A-E911-A5A4-EC0D9A822636.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/50EFD91D-628A-E911-80A0-A0369F3102B6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/70D9B558-F08A-E911-B7D8-EC0D9A8221E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/6AEB245B-CF88-E911-A790-0CC47A7C34C4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/B4FEC605-A789-E911-B6F1-0CC47AC08BFA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/061AEB68-5E88-E911-968B-B083FED179D5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/AEEDBCB6-A988-E911-87BC-1418774126FB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F6B90C9F-7589-E911-BED2-801844DEEFD8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/5025622F-1B89-E911-B110-0CC47A1DF620.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/02CC4EB5-0A88-E911-97C7-FA163E62AD8C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/4C56F3DE-3F88-E911-A97E-FA163ED55DC4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/B8A6AB3F-2D89-E911-9BA1-FA163EA36BDD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/4C4FE4C0-178A-E911-A41A-B49691386D00.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/B8625D60-068B-E911-A1BA-BC305B390A8D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/EC50866E-CD88-E911-94A0-AC1F6B0DE2A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/582C063B-428A-E911-AF37-3417EBE644A7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/D65E38B6-1A8B-E911-A0C8-B026283D9280.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/164F7600-DA8B-E911-B4AC-0023AEFF2C68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/46BBAB7E-DE8C-E911-8156-20CF3027A684.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/0CA028EC-458B-E911-8ADC-AC1F6B0DE0A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/0CD8B82D-698B-E911-BE3D-20CF3027A6B0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/4E4796BB-6388-E911-A0E5-008CFAC94134.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/8012DE54-6189-E911-8CA7-0025905C4300.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F434B80D-B589-E911-8EBD-34E6D7BEAF1B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/48445AC9-1F8B-E911-88A2-AC1F6B8DD22E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/063AAE93-0A88-E911-842A-509A4C9F8888.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/48993DBD-E688-E911-86B0-441EA1616D3A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/36F2C02E-CE88-E911-B40F-10BF481A0245.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/CCC92FF3-2F8B-E911-864A-A4BF01125BE8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/18D6EE87-2E8B-E911-9483-1866DAEA6E00.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/58581D02-968B-E911-98B8-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/E4F06463-518A-E911-847A-FA163E4B54F9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/4EAC233D-6F8B-E911-8AC4-FA163EF1C9CB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F8795E8E-DF8A-E911-A303-A4BF0101F533.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/74B5BB92-DF8A-E911-A9D3-0CC47AFC3D34.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/B019B3D1-768B-E911-BB69-002590207C08.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/86650BD2-928B-E911-B957-3417EBE649FF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/30D5CA38-708C-E911-BBE4-509A4C84EABE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/EC098180-908C-E911-BF89-A0369FD0B1FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/8A2D204A-888D-E911-8420-A0369FE2C0D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/FC8C4F21-B68C-E911-9D88-6C3BE5B50170.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/98B5D620-5D8B-E911-9C4B-008CFAC91964.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/8AA21CFE-368C-E911-907E-008CFA165F18.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/360ECE6B-2D8C-E911-BDF8-0CC47AFCC416.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/9CE6072C-B38C-E911-92C5-0CC47AFF0234.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/6CB85314-BF8C-E911-BABF-0CC47AFCC3A6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/9AFE860C-828E-E911-80BD-008CFA197DE4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/42416BB1-FF8D-E911-AD9B-0CC47A2AECFA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F23E46F3-618E-E911-B454-0CC47A2AED8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/12E17D57-A290-E911-B78C-7CD30AD090D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/88E93E22-8D91-E911-94A5-F04DA274C90B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/52C5AD55-4F96-E911-9BD0-48FD8EE73A95.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F2ED6EED-B38D-E911-A040-008CFA165FD0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F664ADCC-7E8E-E911-B726-24BE05C63741.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/362F3357-D38D-E911-A9A8-AC1F6BAC807A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/CC1D3FCA-9793-E911-A292-0CC47AFC3CA2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/EA9B6402-9E93-E911-A53F-002590207B90.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/0853035B-9A93-E911-B355-0026B927869F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/4C1F38B2-9E93-E911-92E5-7CD30AD0A7AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/788E9439-168E-E911-A81C-20040FE9AD58.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/18843266-8794-E911-B080-002481D2C9DE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/201BB20C-6196-E911-A421-68CC6EA5BE3A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/2A4C7837-E392-E911-84F7-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/766E15CF-CF94-E911-A83C-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/B2EB45EF-3C96-E911-A7A7-AC1F6B1B2392.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/9CF93D24-3B96-E911-BC3E-00266CFFBC3C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/9403152A-4396-E911-8AD1-AC1F6B1AF186.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/24BCFA0C-0591-E911-9813-A0369FE2C094.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/066C8556-7894-E911-811F-A0369FD0B344.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/A8A55033-4995-E911-8E7B-A0369FE2C152.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/5CC5EA12-E08D-E911-9AC6-FA163E001A47.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/80D90D29-0A8E-E911-9855-901B0E5427B0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/CC627C40-AA8D-E911-9917-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/020D38EF-8891-E911-8CBF-FA163E2DC1EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/70E8FF8A-DA92-E911-9E32-FA163EC9524C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/7E6ABAB2-D791-E911-96A3-6C3BE5B50170.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/2C76F8C2-4B93-E911-ADCA-44A842CF0634.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/346EF0C2-088E-E911-8D0C-509A4C8339DE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/42CEED8B-158E-E911-AAF4-001E67A3ED40.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/10B5A311-D592-E911-AEE7-20CF3027A6E2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F43E960B-D592-E911-BF37-98039B3B01C2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/26129868-E5A0-E911-8FF9-0CC47AFB7D80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/AAABE48C-EDA0-E911-B19F-0025905C548A.root',
] )














