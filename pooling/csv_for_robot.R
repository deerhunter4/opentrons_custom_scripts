setwd("path/to/the/file")

# install.packages("readxl")

library(readxl)

csv_to_robot <- function(file_name, sheet_name){
  
  data <- read_excel(file_name, sheet_name, col_names = FALSE)
  data <- as.data.frame(as.matrix(data))
  data
  
  pooling_table <- data.frame(matrix(ncol = 4, nrow = 0))
  
  IDs<- c("A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", 
          "C2", "D2", "E2", "F2", "G2", "H2", "A3", "B3", "C3", "D3", "E3", 
          "F3", "G3", "H3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", 
          "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "A6", "B6", "C6", 
          "D6", "E6", "F6", "G6", "H6", "A7", "B7", "C7", "D7", "E7", "F7", 
          "G7", "H7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "A9", 
          "B9", "C9", "D9", "E9", "F9", "G9", "H9", "A10", "B10", "C10", 
          "D10", "E10", "F10", "G10", "H10", "A11", "B11", "C11", "D11", 
          "E11", "F11", "G11", "H11", "A12", "B12", "C12", "D12", "E12", 
          "F12", "G12", "H12")
  
  destination <- c("A1", "B1", "C1", "D1", "A3", "B3") # here you can change destination wells
  
  data[,"last_column"] <- NA
  k <- which(data == "plate", arr.ind = TRUE)
  
  if (length(k[,1]) == 0){
    
    next()
    
  } else {
    
    for (j in 1:length(k[,1])) {
      
      row <- k[j,1]
      col <- k[j,2]
      col_1 <- col
      
      while (!is.na(data[row,col])) {
        # print(data[row,col])
        col = col+1
      }
      
      plate <- data[row:(row+8),col_1:(col-1)]
      
      samples <- as.numeric(as.vector(as.matrix(plate[-1,-c(1,2)])))
      
      plate <- plate[1,2]#i
      
      table_fragm <- cbind(plate, IDs[1:length(samples)], destination[plate], samples)
      pooling_table <- rbind(pooling_table, table_fragm)
    }
    
    colnames(pooling_table) <- c("Plate Position",	"Source Well ID",	"Destination Tube ID",	"Volume")
    pooling_table <- na.omit(pooling_table)
  }

  write.csv(pooling_table,"./csv_for_robot.csv", row.names = FALSE, quote= FALSE)
}


csv_to_robot("Pooling_example.xlsx", "GR")
