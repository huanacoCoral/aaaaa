using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System;
using System.Windows.Forms;

namespace PRUEBA2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            LoadData();
        }

        private void LoadData()
        {
            try
            {
                ClassLibrary1.Class1 c1 = new ClassLibrary1.Class1();
                this.dataGridView1.DataSource = c1.alumno().Tables[0];
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error al cargar los datos: " + ex.Message);
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            // Este evento se puede dejar vacío si no necesitas manejar clics en celdas
        }
    }
}
