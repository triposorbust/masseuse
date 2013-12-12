library(ggplot2)

make.series <- function(some.label, some.filename) {
    df <- read.table(some.filename, header=FALSE)
    df$V1 <- as.Date(df$V1)
    df$V3 <- some.label
    names(df) <- c("Time","Value","Group")
    return(df)
}

raw <- make.series("raw","generated.tsv")
msg <- make.series("massaged","massaged.tsv")
dat <- rbind(msg,raw)

plot <- ggplot(dat)
plot <- plot + geom_line(aes(x=Time,y=Value,group=Group,color=Group), stat="identity", size=1, alpha=0.75)
ggsave("massaged.pdf", plot=plot, width=10, height=4, units="in")
