import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/0E8FFAB5-C8F6-E611-B66D-B499BAAC0676.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/00EE9EAE-8FF6-E611-AF99-0025907DC9D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/AA9F4EAB-19F6-E611-AB0D-02163E019CF3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/DAEAB2C6-19F6-E611-9594-002590D9D8A4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2C38CE45-DAF6-E611-9CB0-20CF305B0512.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/1AE2E569-D5F5-E611-894C-1CB72C1B2EF4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/3810FB0C-A8F6-E611-86BA-34E6D7BDDEC1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/1831DF43-00F6-E611-B364-0CC47A537688.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/3A0264A5-9FF5-E611-A8E1-00259095306C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/326D989B-53F5-E611-9C61-44A842BECCBE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/142BC279-65F5-E611-8462-7845C4F914AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/FC39F519-82F5-E611-9CA8-44A842B2D64B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/447BACFB-A0F5-E611-B0EC-44A842BE76FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C40EAD00-A1F5-E611-B5AA-00145EDD750D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/E4971CF6-37F6-E611-BFB4-F04DA274BB9C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2C17425C-71F6-E611-93DF-003048CDCE68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/5647BB6C-75F5-E611-A631-0025904C6224.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/0C0848F9-85F5-E611-BCFF-0025905C2D98.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2A6F26FA-94F5-E611-9CDF-0025905C4300.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/44282D14-9CF5-E611-B133-0025905C54B8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/96C814EE-A6F5-E611-898B-0025905C54F4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/1C7DF681-41F6-E611-B403-0CC47A706FF4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E24E05F7-11F6-E611-80DD-6CC2173BC220.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AC16598E-76F6-E611-B608-002590A83370.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AA7CE32C-7BF6-E611-B160-002590A37106.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/229F3FF0-7AF6-E611-9603-001E67398520.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/BCF84D9D-80F6-E611-9459-002590A371D4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/32F3A69F-7DF6-E611-A6F3-002590A83370.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/2669A21B-83F6-E611-8C7B-001E677926FA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AC8880A6-83F6-E611-BEEB-001E67E6F8E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/002E3F01-A8F6-E611-922C-001E67E71C36.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/42801879-80F7-E611-ACCA-001E67E6F7F6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/680AE1A7-4DF6-E611-BD64-0CC47A4C8F18.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/DE54A76C-ACFB-E611-8F09-02163E00E607.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/50432FF4-ABF5-E611-BA4B-002481CFE708.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/00CD96EC-D7F8-E611-B208-00266CFFBF94.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/8C78F848-C8F9-E611-B4DF-DEDBE4AC1313.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/284E0427-28F8-E611-BD7B-047D7B881D8E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/FA200342-28F8-E611-8AD8-0242AC110005.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/E458FBC2-AAF8-E611-9BF7-047D7BD6DF34.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/5E507654-20F6-E611-95D8-3417EBE6444A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/069EAAD2-A3F7-E611-B19A-34E6D7BDDECE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/682C6CE6-20F6-E611-AA22-14DDA9D4F20C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/82A0C8FC-ABFB-E611-9A41-FA163EC0B67E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/9E6A71FA-ABFB-E611-8DE5-FA163E1DA50E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/D6860238-ACFB-E611-A2A7-02163E00C39F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/5C8C0360-ACFB-E611-A1BD-02163E00C937.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/78746B76-ACFB-E611-A837-02163E00B0B0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/10AA6C6B-ACFB-E611-86AC-02163E00B225.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/12BAC61D-ACFB-E611-8600-FA163E023ED2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/04ADB904-ACFB-E611-BF75-FA163EB499D4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/98337B2D-ACFB-E611-9FC2-FA163E8409A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/A839FC18-ACFB-E611-BE4F-FA163EAED918.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/E490E901-ACFB-E611-82CB-FA163E4AB13F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/34224808-ACFB-E611-AF14-FA163E49DE1D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/9ED4D111-ACFB-E611-B3DD-FA163EE81F7F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/92C4E901-ACFB-E611-894E-FA163E4AB13F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/34F2C61D-ACFB-E611-BAE7-FA163E023ED2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F007C81D-ACFB-E611-978B-FA163E023ED2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/56FE8A08-ACFB-E611-BD2E-FA163EA3A0F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C22CFEB2-57FC-E611-AC04-FA163E1C00CB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/64E20A88-F7FF-E611-8B3F-002590A37116.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/6879A74A-DDFC-E611-AEF2-02163E0134F8.root',
] )




































