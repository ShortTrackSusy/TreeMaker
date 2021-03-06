import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/24F9209E-8EC5-E611-A482-001C23C0F203.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8CE81C0E-57C6-E611-B772-782BCB539226.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8612752E-93C5-E611-B41A-0CC47A0AD69E.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2A7DB915-5DC6-E611-B271-002590D9D968.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6C7E4FF6-94C5-E611-B039-02163E0176A9.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CC5CD076-4FC6-E611-AA09-FA163E132F46.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4E39B606-5DC6-E611-9E6A-FA163E63948C.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/923D073E-A1C5-E611-B45F-001E675A6AB3.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/98A88183-8EC5-E611-83B6-0CC47A6C14C8.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/48F68644-93C5-E611-B139-1C6A7A26E465.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/58D1866F-A0C5-E611-9F33-00259048BF92.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9CBA9D69-E9C5-E611-AFAA-001E674FC800.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B4784B93-F0C5-E611-947A-001E674440E2.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B271198C-28C6-E611-8A84-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AE1D97B5-24C6-E611-A2F4-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7A913222-32C6-E611-956A-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AC7CC899-34C6-E611-8728-0242AC130003.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3A355CD8-2FC6-E611-832B-001E674FCB5C.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/10F0450A-3DC6-E611-BB5A-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F68CB99F-38C6-E611-80F0-0242AC130003.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AA379907-3DC6-E611-90C7-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CAD00C12-3DC6-E611-BF86-0242AC130003.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/58EB9A99-42C6-E611-9067-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5E20D820-48C6-E611-B37E-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/64810B72-48C6-E611-8C1A-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/026AE4E8-44C6-E611-A007-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C09F2863-4CC6-E611-A13B-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A26AD780-46C6-E611-950C-001E67444EAC.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1AAB3257-43C6-E611-BDF3-001E67456F68.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AA053963-4BC6-E611-B22F-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BE04CA82-46C6-E611-8539-001E67444EAC.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9006737E-46C6-E611-82FF-001E67444EAC.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/382BB60A-50C6-E611-816E-001E67457E36.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F261B859-4FC6-E611-A4F2-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4A49236C-51C6-E611-B29F-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/62226613-4EC6-E611-9945-001E67444EAC.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A26BD57B-51C6-E611-8B85-001E67456F68.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A22C255E-4FC6-E611-AF82-001E674FC800.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B6BA79AC-55C6-E611-97EA-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C66D8E09-53C6-E611-94E0-D067E5F9189F.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FA609064-5BC6-E611-A3BF-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/24E25F76-5BC6-E611-B29D-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/40088368-59C6-E611-A13A-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7A9F5008-57C6-E611-AF82-001E674FBFC2.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A6CEE2BC-55C6-E611-A284-001E67586A2F.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CE3FA64A-57C6-E611-9BF0-001E67444EAC.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D8BFA691-5DC6-E611-BDAE-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A88BE12E-62C6-E611-8766-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AE0012BE-63C6-E611-8142-001E674FCAE9.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2A60AE5E-64C6-E611-B978-001E67457DFA.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3CEBB144-60C6-E611-A377-001E67457E9F.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/36DD440E-68C6-E611-A6F2-001E674FC800.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/887ABE0C-6FC6-E611-A4D8-ECF4BBE16610.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/966C0A31-6DC6-E611-95EB-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/409D70D0-5FC6-E611-AFEA-001E674FCA99.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/44F63EF2-67C6-E611-B3FC-001E67456F68.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/94451A80-6EC6-E611-B71A-001E674FCAE9.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6AD4A5F4-49C7-E611-A84C-001E674FCA99.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/38A09045-8FC5-E611-AEEC-E0071B7A68F0.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6639A4C8-95C5-E611-A393-E0071B7AC5D0.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/566E6DA1-5FC6-E611-9CB6-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A4C003C6-7DC5-E611-A4DB-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C66DB6CB-7DC5-E611-8909-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/96C1EE58-8AC5-E611-9656-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C4CF9363-8AC5-E611-B967-001E674FC9F4.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/449F3587-8EC5-E611-92B3-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F6900D84-8EC5-E611-9952-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/34F88A13-91C5-E611-B773-ECF4BBE16148.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7C2FCCDA-95C5-E611-B8EB-001E674FAF23.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/48AA311C-9EC5-E611-B5D4-001E674FAF23.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F8992189-5FC6-E611-A1FD-D067E5F91ABB.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9CB9176F-8EC5-E611-89E6-0CC47A7C35F8.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/24709132-95C5-E611-BDAA-0025905B8604.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D640910F-8BC5-E611-AAB0-0CC47A4D76C0.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3429A6B7-A0C5-E611-B94D-0CC47A4D766C.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A04E2CC8-A0C5-E611-A427-0025905A609A.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/AED36666-61C6-E611-A808-0CC47A4D7674.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FECA828B-93C5-E611-9C2B-008CFA197448.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0A52EA39-95C5-E611-99BB-008CFA111314.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A8BA683C-5DC6-E611-B516-008CFA1974D8.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D29AF794-EDD0-E611-8AC0-001E67457107.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FEC38CD6-F3D0-E611-9714-ECF4BBE16610.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8AFCA606-F9D0-E611-ACC9-001E67586A2F.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/444BDBD0-05D1-E611-922F-001E674FCA99.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B604B61B-0FD1-E611-9977-001E674FC800.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DAD8E08C-20D1-E611-A4AE-001E674440E2.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BC178EBB-32D1-E611-835E-001E67348055.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A0EF74A3-39D1-E611-892D-001E674FB24D.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5C29037C-4BD1-E611-9ABE-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A0F02034-5BD1-E611-B936-0242AC130007.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/70BC4614-5AD1-E611-9C0E-D067E5F914D3.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DCF729CB-63D1-E611-BE79-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/92FAE6C4-67D1-E611-AA81-001E67457A5D.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6AC459A2-75D1-E611-B94D-001E67456F68.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A6E0601B-A2D1-E611-90E8-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C6EB78A9-A8D1-E611-B0D0-001E67457A5D.root',
'/store/mc/RunIISummer16DR80Premix/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6A4E5939-B4D1-E611-AF74-001E674FAF23.root',
] )




































