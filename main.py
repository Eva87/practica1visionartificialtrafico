import argparse
import glob
import deteccionMSER
import deteccionAlternativa
import deteccionAlternativaconMSER

'''Llamada profe
python main.py –train_path /home/usuario/train --test_path /home/usuario/test –detector detector
python main.py –train_path /home/usuario/train --test_path /home/usuario/test –detector MSER
python main.py –train_path /home/usuario/train --test_path /home/usuario/test –detector Alternativa
python main.py –train_path /home/usuario/train --test_path /home/usuario/test –detector detector

python main.py -–train_path ./train --test_path ./test -–detector MSER
python main.py -–train_path ./train --test_path ./test -–detector Alternativa
python main.py –train_path C:/Users/evaho/Desktop/kraken/va/practica1visionartificialtrafico/train --test_path C:/Users/evaho/Desktop/kraken/va/practica1visionartificialtrafico/test –detector Alternativa
python main.py –train_path /home/usuario/train --test_path /home/usuario/test –detector detector
'''

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Trains and executes a given detector over a set of testing images')
    parser.add_argument(
        '--detector', type=str, nargs="?", default="", help='Detector string name')
    parser.add_argument(
        '--train_path', default="", help='Select the training data dir')
    parser.add_argument(
        '--test_path', default="", help='Select the testing data dir')

    args = parser.parse_args()

    # Load training data

    # Create the detector

    # Load testing data

    # Evaluate sign detections

    #print(vars(args))
    strtrain=args.train_path
    strtest=args.test_path
    for strinentradaimg in sorted(glob.glob("./"+strtrain+"/*")):
        finnombre = strinentradaimg[-3:]
        for strinentradaim in sorted(glob.glob(strinentradaimg)):
            if finnombre != "txt" and (finnombre == "jpg" or finnombre == "ppm"):
                if args.detector =="MSER":
                    deteccionMSER.MSER(strinentradaim)
                elif args.detector=="Alternativa":
                    deteccionAlternativa.Alternativa(strinentradaim)
                else:
                    deteccionAlternativaconMSER.AlternativaMSER(strinentradaim)


    for strinentradaimg in sorted(glob.glob("./"+strtest+"/*")):
        finnombre = strinentradaimg[-3:]
        for strinentradaim in sorted(glob.glob(strinentradaimg)):
            if finnombre != "txt" and (finnombre == "jpg" or finnombre == "ppm"):
                if args.detector =="MSER":
                    deteccionMSER.MSER(strinentradaim)
                elif args.detector=="Alternativa":
                    deteccionAlternativa.Alternativa(strinentradaim)
                else:
                    deteccionAlternativaconMSER.AlternativaMSER(strinentradaim)

        '''for strinentradaimg in sorted(glob.glob("./" + "test" + "/*")):
            finnombre = strinentradaimg[-3:]
            for strinentradaim in sorted(glob.glob(strinentradaimg)):
                if finnombre != "txt" and (finnombre == "jpg" or finnombre == "ppm"):

                    deteccionMSER.MSER(strinentradaim)'''



