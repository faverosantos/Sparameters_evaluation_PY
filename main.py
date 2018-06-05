import matplotlib.pyplot as plt
import math

# References
# [1] https://www.rapidtables.com/convert/electric/db-converter.html
# [2] 65nm_PA_core_V02_R00

def calculate_mu(S):
    S11 = S[0][0]
    #print("S11 magnitude value @ 2.4 GHz: " + str(round(abs(S11),5)))
    #print("S11 magnitude value via Cadence @ 2.4 GHz: 228.387m")
    #print("S11 dB20 value via Cadence @ 2.4 GHz: -12.9314")
    # Se o valor de magnitude a partir do dB20 é calculado, obtem-se 0,050917
    # Como é obtido o valor de magnitude no cadence??


    S12 = S[0][1]
    #S12 = abs(S12)

    S21 = S[1][0]
    #S21 = abs(S21)

    S22 = S[1][1]
    #S22 = abs(S22)

    delta = S11*S22 - S12*S21
    mu_a = 1 - math.pow(abs(S11), 2)
    mu_b = abs(S22 - S11.conjugate()*delta)
    mu_c = abs(S21*S12)
    mu = mu_a/(mu_b+mu_c)
    return mu


def main():
    S_1G5 = [[complex(806.5E-3, -456.6E-3), complex(-644.5E-6, -2.142E-3)],
             [complex(184.7E-3, -168.5E-3), complex(996E-3, -89.58E-3)]]

    #S_2G4 = [[228.3887E-3, 93.9387E-3 ],
    #         [6.0911, 828.012E-3 ]]

    S_2G4 = [[complex(3.41E-3, 50.80E-3), complex(3.47E-3, 89.97E-3)],
             [complex(-4.414, 3.802), complex(343.03E-3, 633.83E-3)]]

    S_3G1 = [[complex(-159.9E-3, 144.8E-3), complex(14.93E-3, 4.222E-3)],
             [complex(383.7E-3, 604E-3), complex(986.6E-3, 90.61E-3)]]

    #mu_S1G5 = calculate_mu(S_1G5)
    #print("Mu @ 1.5 GHz: " + str(round(mu_S1G5,5)))
    #print("Mu @ 1.5 GHz via Cadence: 992.326E-3")

    mu_S2G4 = calculate_mu(S_2G4)
    print("Mu @ 2.4 GHz: " + str(round(mu_S2G4,5)))
    print("Mu @ 2.4 GHz via Cadence: 640.091E-3")
    print("Mu @ 2.4 GHz via Matlab: 0.8184")

    #mu_S3G1 = calculate_mu(S_3G1)
    #print("Mu @ 3.1 GHz: "+str(round(mu_S3G1,5)))
    #print("Mu @ 3.1 GHz via Cadence: 995.098E-3")

if __name__ == "__main__":
    main()
