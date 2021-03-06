import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/D837877F-0152-E911-9C08-AC1F6B1E303E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/641CA1A3-6152-E911-BEAF-008CFAF5550C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/DA59A105-0751-E911-BF4D-00266CFCC8A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/1A687435-2D52-E911-8702-A0369FF8852E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/BCF989A1-E750-E911-B7AF-008CFA197AC4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/24AC12E1-0451-E911-BB91-008CFA111158.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/98379351-DC51-E911-A16C-008CFA197464.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/DC0DD8D6-6052-E911-89E1-008CFAC91EBC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/AC4010A8-EC50-E911-B17B-0242AC1C0501.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/9AE74E35-F550-E911-837F-0242AC1C0506.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/EEAFA9EF-FA50-E911-968C-0242AC1C0500.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/7E604206-0151-E911-BB65-0242AC1C0500.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/94793309-0151-E911-8BDF-0242AC1C0501.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/D2E74BCE-0351-E911-B265-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/7CDD962B-0751-E911-AE03-0242AC1C0503.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/C20E4EA7-0C51-E911-993C-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/CAF616D7-0F51-E911-A268-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/EEE80AE3-1251-E911-82DF-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/5667718E-DD51-E911-8FE9-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/FA15AB22-6252-E911-929B-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/7AEC2D1B-D850-E911-972C-24BE05C656A1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/D6EA9457-E450-E911-B381-506B4BB134E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/6EEE3324-FB50-E911-B96A-EC0D9A8222F6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/7623EE63-C851-E911-AAE2-506B4BB16AE6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/CC9CB36C-6152-E911-8A14-506B4BB16AEE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/12F4ACFC-DC50-E911-840D-FA163E4BD65F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/E09721FA-DF50-E911-BCF2-FA163E94A27B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/BE467EE7-E550-E911-9966-FA163E1ED4DD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/7EAD244F-E350-E911-A082-FA163ED4856F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/A05C5F3D-E950-E911-8BB3-FA163E73EDD2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/AA0836E2-EE50-E911-A312-FA163EC67281.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/281F491E-F250-E911-9151-FA163E920180.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/C2889EF4-F450-E911-AA23-FA163EDCCBF3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/402BE497-FA50-E911-9154-FA163EB709A6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/8099CC8C-0051-E911-994D-FA163E19CCB2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/1CC238B7-0951-E911-BE9E-FA163E1ED4DD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/E676B97C-1C51-E911-AC30-FA163E4D9482.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/F83EDBD5-6152-E911-A530-FA163E34033B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/FEDF55D8-FD50-E911-9174-00259048AE50.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/38F8629C-2551-E911-B845-0CC47A57CB62.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/46CE778E-6152-E911-B96B-0CC47A57CB8E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/605DD51B-6452-E911-8332-AC1F6B0DE140.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/FA3596DD-F750-E911-907B-0CC47A7C3432.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/DA77538A-FD50-E911-BA75-AC1F6BAC7D10.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/00705CE2-0051-E911-A64D-AC1F6BAC7D10.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/0A50552B-0751-E911-B4F5-0CC47A4D769A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/B6AC99BD-0951-E911-B754-AC1F6BAC7C06.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/D87E0C6A-1951-E911-AEF7-AC1F6BAC8158.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/ACD66860-2251-E911-B697-0CC47A4D7606.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/C6DB1DA6-3551-E911-9945-0CC47A4C8E2A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/6834C0F9-4451-E911-8F72-AC1F6BAC7C4A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/9C4AD793-6152-E911-9A7B-0CC47A7C3428.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/9A0306C7-0351-E911-9643-A0369FE2C146.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/B8F6B519-6252-E911-96AF-48D539D3336D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/28612B0B-E650-E911-99FC-0CC47A4D7636.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/E483704D-E950-E911-956A-0CC47A4C8E86.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/5099D50E-EC50-E911-BEE3-0025905B85A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/28B9C926-F250-E911-B614-0CC47A78A446.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/1EEB3751-F550-E911-9B91-0CC47A4D7626.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/BE814321-0B51-E911-A84A-C45444922C46.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/86577B9B-E251-E911-8595-0025904C7A8E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/78ADF128-6452-E911-8AB4-C454449229EB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/0A077AD6-F850-E911-A613-34E6D7BDDEC1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/88B8AEB3-0C51-E911-9B42-D8D385AF8902.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/E8A0C8D5-D751-E911-BC8E-AC1F6B4E013E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/96AA0923-6452-E911-B47A-AC1F6B8DD2A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/4E51C045-EC50-E911-AD94-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/66C7CF5D-0451-E911-AEA2-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/BC0743C4-2F51-E911-93A4-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/38BBBF8F-6152-E911-ADE7-0242AC130003.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/CA756003-F850-E911-B40A-848F69FBC0F7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/D0A00D19-2C51-E911-8C77-24B6FDFFBB88.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/BCA4EF2D-C251-E911-B7D9-00266CFE7818.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/943679C2-6152-E911-B793-5C260AFFFB72.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/A616F7A7-CB51-E911-8128-44A842CFD5D8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/949C5D55-6152-E911-82EE-001CC47B0FD2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/6005FD29-DD50-E911-A784-0CC47AFF04A4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/96FE3C45-E950-E911-8B9C-0CC47AFF02F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/42A12C64-F550-E911-869A-0CC47AFF02F4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/62CA3E3E-BF51-E911-BB60-0CC47AFB7F5C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/D857F120-6252-E911-8DF0-0CC47AFF0258.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/6C74EE38-E950-E911-8A20-0CC47AD98D26.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/20E077FA-F150-E911-99F6-0CC47AD98B94.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/DEA88947-F850-E911-AD3A-1C6A7A26CE77.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/D2E6868F-0351-E911-90C6-002590E3A0EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/B82F1B1D-0D51-E911-A26A-1C6A7A26CA0F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/9E4185C3-2251-E911-A6E7-0CC47AD98F72.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/B612E99D-3C51-E911-BB1C-0CC47A6C063E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/DCA59B7A-6152-E911-89AF-002590E39D90.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/1223FD2F-E450-E911-AE88-B02628341FD0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/DA22EC5A-E950-E911-9EA8-509A4C845431.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/CEEBCD17-F250-E911-AF9E-509A4C83EF12.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/2C9DAEA1-0451-E911-BEDF-7CD30ACDCACA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/44218A30-0D51-E911-96E1-008CFAFBE8F2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/12DC7B83-E951-E911-BED4-008CFAF2018E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/F606A98F-F250-E911-80B5-20040FE9CF48.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/3CE84E35-0751-E911-8B15-1866DAEB40CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/A081A52E-1951-E911-B957-549F3525D084.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/E6B62378-6152-E911-B904-14187741121F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/5EE29E60-F250-E911-BD93-001E67E7136D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/C2CA1840-BF51-E911-A038-A4BF0112BE12.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/685481F5-6152-E911-93C4-001E67E6F873.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/DAD39B94-3A51-E911-9CCB-0030487BA14E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/4EE7F621-F850-E911-8A42-28924A35056E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/2E6D0640-D251-E911-B489-0026B927865E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/C0E62560-1951-E911-9113-0CC47AFC3D32.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/58880AFD-6152-E911-B3D3-D48564594FB4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/C82FB542-E751-E911-90C1-0017A4770454.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v4/70000/9CCDB56E-6152-E911-8BEC-0CC47A5FC61D.root',
] )




































