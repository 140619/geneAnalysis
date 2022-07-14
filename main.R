library(enrichplot)

df <- read.csv("F:/geneAnalysis/Documents/example/GO-MF-SND1.csv", header = TRUE)

gene<-bitr(df$ID,fromType = 'ENTREZID',toType = 'SYMBOL',OrgDb = 'org.Hs.eg.db')

print(cnetplot(x,showCategory = 1))

enrichDGN
GO_database <- 'org.Hs.eg.db'

library(DOSE)
data(geneList)
de <- names(geneList)[abs(geneList) > 2]

edo <- enrichDGN(de)

library(clusterProfiler)
library(enrichplot)
snd1 <- read.csv("F:/geneAnalysis/Documents/example/SND1.csv",header = TRUE)
gene1 <-bitr(snd1$gene_symbol,fromType = 'SYMBOL',toType = 'ENTREZID',OrgDb = 'org.Hs.eg.db')
GO <- enrichGO(
  gene1$ENTREZID,
  OrgDb = 'org.Hs.eg.db',
  keyType = "ENTREZID",
  ont = "MF",
  pvalueCutoff = 0.05,
  pAdjustMethod = "BH",
  qvalueCutoff = 0.05,
  minGSSize = 10,
  maxGSSize = 500,
  readable = TRUE
)

# library(enrichplot)

# edox <- setReadable(edo, 'org.Hs.eg.db', 'ENTREZID')
# p1 <- cnetplot(edox, foldChange=geneList)
