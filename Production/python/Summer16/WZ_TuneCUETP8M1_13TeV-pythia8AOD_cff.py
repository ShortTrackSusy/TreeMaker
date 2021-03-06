import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1C897643-AED7-E611-847F-549F3525B154.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/925B34FA-8CD7-E611-BF42-90B11C27F383.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/642B27F7-8CD7-E611-8AD2-A4BF0101DD64.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A46D72C9-51D7-E611-A614-0025901AC3F8.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CEF04EB7-57D7-E611-8A28-0025901AC0FC.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8C270A72-29D7-E611-9336-5065F37D9171.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9810EC58-2AD7-E611-962E-5065F3812271.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CAB6D376-29D7-E611-985D-E0071B7AC7B0.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/02137180-2AD7-E611-A8EC-5065F3819221.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1A352786-2AD7-E611-8FA9-24BE05C6E7C1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CEC7F683-2AD7-E611-B637-E0071B74AC00.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C407CC87-2AD7-E611-B840-24BE05C61601.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DC136688-2AD7-E611-9DD0-E0071B740D90.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F4A31708-29D7-E611-AC57-B8CA3A70A410.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A2C8C435-2BD7-E611-B122-24BE05CEFB41.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FA489B21-2CD7-E611-B320-24BE05C6D5B1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/66C49F6D-2BD7-E611-BAFB-E0071B7AC750.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/50E450D9-2CD7-E611-BE4A-E0071B7AC7B0.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/004DD4A8-57D7-E611-86CF-5065F3818271.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3E8F5FAC-57D7-E611-9475-A4BF01025B08.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EC80A0DA-2FD7-E611-BD8C-002590E2DDC8.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/629D77BC-57D7-E611-B8B1-002590491B1C.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/702E9610-23D7-E611-97E6-E0071B7A9810.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/584FFFBD-26D7-E611-8191-24BE05C6D5B1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3493BF8C-27D7-E611-973B-24BE05BD4F61.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/12EADFC4-26D7-E611-930D-5065F3812271.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C64EFBB9-25D7-E611-AEE2-4C79BA1813D5.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B8913D91-27D7-E611-9AB6-5065F3810301.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4C20B2F3-28D7-E611-9ACB-E0071B7A58B0.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/721E42CC-28D7-E611-B718-24BE05C6D5B1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4E779F95-27D7-E611-A17C-24BE05CEFB41.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9ACFA991-27D7-E611-A36E-E0071B7AC750.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/88854A73-29D7-E611-9F74-24BE05C60641.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BA20AFDF-5DD7-E611-AF53-A0369F3016EC.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/68ECD3F2-60D7-E611-93AF-24BE05C3FBB1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F807A0C5-61D7-E611-BA19-24BE05CEED81.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9EE115CC-60D7-E611-8692-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/46459DA6-61D7-E611-BFAF-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA90BAD8-60D7-E611-B236-A0369F301924.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/22035709-8DD7-E611-A2AC-02163E0174C6.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/946B2F5B-8DD7-E611-AF95-FA163E9988DA.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9A312CB4-66D7-E611-873C-24BE05BD4F61.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AA2D86AC-67D7-E611-911F-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/626588B0-67D7-E611-A9C2-A0369F310374.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C8CCF282-67D7-E611-A23E-B8CA3A70B608.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/22C47EB4-67D7-E611-9071-A0369F3016EC.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/368DDE60-6AD7-E611-A47E-5065F38142E1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/88510531-6CD7-E611-8942-5065F3820341.root',
'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BE142289-6CD7-E611-B722-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0A352C3B-6CD7-E611-A57B-A0369F3016EC.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AE06AC9B-70D7-E611-A5D4-24BE05CE4D91.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/90D2B4AC-6CD7-E611-83A6-B8CA3A70B608.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9EC1D243-74D7-E611-A016-24BE05C618F1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/58C1073C-74D7-E611-8A81-5065F37D9171.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/62E3F97A-7BD7-E611-9264-A0369F3016EC.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B2D0EF9D-84D7-E611-A601-5065F381E271.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B69AB983-84D7-E611-B525-B8CA3A70B608.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/52FEF57E-84D7-E611-B164-B8CA3A709028.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FEA05B7F-84D7-E611-93E0-A0369F3102B6.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/08544EE5-8CD7-E611-B9EF-E0071B740D90.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/60867DB3-8CD7-E611-A5EC-0CC47A57D136.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/12EBAE29-2ED7-E611-8647-0025905B857E.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7ABBA3B0-2ED7-E611-B52D-0CC47A4D75F8.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E06DAC8B-32D7-E611-BB15-0025905A60B6.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E0D777F0-56D7-E611-836D-0025905A60F8.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/845FEDC1-57D7-E611-BF5C-008CFA1111A0.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/20313158-33D7-E611-95C1-24BE05BD4F61.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0E21C964-33D7-E611-AEDB-5065F3816201.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3A1E208B-37D7-E611-8338-24BE05C4D8F1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9E547E6A-37D7-E611-AA36-5065F382C2F1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/40378448-3DD7-E611-A152-E0071B7AC7B0.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AAF37D0D-3FD7-E611-B4B9-24BE05CEDC81.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA076488-40D7-E611-B541-24BE05C49891.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/505F4A0C-44D7-E611-B338-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7E6A8618-45D7-E611-A124-B8CA3A709028.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1855660A-49D7-E611-B50E-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F4A70AA0-49D7-E611-8D88-24BE05C6E561.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FAE43C58-49D7-E611-9F04-E0071B7A4550.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/66C0B693-4CD7-E611-9316-24BE05C6E561.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/086C0680-4FD7-E611-8432-24BE05C488E1.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4C392C80-4FD7-E611-9D58-24BE05C48841.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/767ADE80-4FD7-E611-BD65-24BE05C4D821.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DC71583A-50D7-E611-ADFB-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D8197229-53D7-E611-A5DC-5065F381B211.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/020A8E99-52D7-E611-8885-E0071B7A6850.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2AD11C99-52D7-E611-8A8C-24BE05C6E591.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3623066F-53D7-E611-A6A2-A0369F301924.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D6245D1E-56D7-E611-98C1-E0071B7A6850.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2CAF12E5-58D7-E611-9774-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/40D334B8-5DD7-E611-9FA7-24BE05CE4D91.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/24192DBE-5DD7-E611-8FDE-24BE05C33C71.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FC572EBF-5DD7-E611-AA73-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/ACF92A13-57D7-E611-BC14-D067E5F912FF.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9E4834F2-8CD7-E611-9D12-008CFA197D88.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0C2EE1BA-8CD7-E611-9767-001E674DA1AD.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5655FC45-34D7-E611-8313-FA163EC24F89.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BC6A2AB0-57D7-E611-89B2-02163E012EA8.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1AA37CA9-5CD7-E611-91CC-02163E00B11E.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B2FB6D04-57D7-E611-B577-1866DAEA8190.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FAC022E4-8CD7-E611-8A7F-0025905A610C.root',
#'/store/mc/RunIISummer16DR80Premix/WZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D879960B-8DD7-E611-AEBC-0CC47A7452DA.root',
] )




































