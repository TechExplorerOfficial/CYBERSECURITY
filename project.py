from packet_capture import capture_packets
from analysis import analyze_packets
from visualizer import plot_analysis
import utils.logger as logger

def main():
    logger.log("Iniciando captura de pacotes...")
    packets = capture_packets(duration=60)  # Captura de pacotes por 60 segundos
    logger.log(f"{len(packets)} pacotes capturados.")
    
    logger.log("Analisando pacotes...")
    report = analyze_packets(packets)
    
    logger.log("Gerando gráficos...")
    plot_analysis(report)
    
    logger.log("Análise completa.")

if __name__ == "__main__":
    main()