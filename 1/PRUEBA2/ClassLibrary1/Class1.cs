using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;    
namespace ClassLibrary1
{
    public class Class1
    {
        public DataSet alumno()
        {
          // string connectionString = "Server=LAPTOP-GK59499C;User Id=sa;Password=coral;Database=academico;";
           
            SqlConnection con = new SqlConnection();
            con.ConnectionString = "Server=LAPTOP-GK59499C;User Id=sa;Password=coral;Database=academico;";
            

            SqlDataAdapter ada = new SqlDataAdapter();
            ada.SelectCommand = new SqlCommand();
            ada.SelectCommand.Connection = con;
            ada.SelectCommand.CommandText = "select * from estudiantes";
            DataSet ds = new DataSet();
            ada.Fill(ds);
            return ds;
        }
    }
}
