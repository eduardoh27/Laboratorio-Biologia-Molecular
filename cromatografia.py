import matplotlib.pyplot as plt
import numpy as np

def main():
    
    plt.style.use(['science','no-latex'])
    
    muestras = np.linspace(1,10,10, dtype=int)
    absorbancias = np.array([0.509,0.644,0.513,0.479,0.921,0.527,2.504,0.401,0.408,0.379])
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Tubos$',fontsize=10)
    ax.set_ylabel('$Absorbancia \,\, a \,\, 280nm$',fontsize=10)
    ax.set_xticks(muestras)
    ax.set_xticklabels(muestras)
    
    ax.scatter(muestras, absorbancias, c='#421C5E',s=13, marker='o')              
    plt.plot(muestras, absorbancias, c='#A568D2')

    plt.savefig('cromatografia.png', dpi=300, bbox_inches='tight')
    
    plt.show()

        
if __name__ == "__main__":
    main()
    