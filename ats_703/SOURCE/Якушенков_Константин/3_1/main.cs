/*
Студент: Якушенков Константин
Группа №407
Задание №3.1
*/
using System;
using System.IO;

namespace _3._1
{
    class task3_1
    {
        static void Main(string[] args)
        {
            double[] vects = new double[6];
            string file_string = string.Empty;
            string path = Convert.ToString(Directory.GetParent(Convert.ToString(Directory.GetParent(Convert.ToString(Directory.GetParent(Directory.GetCurrentDirectory()))))));
            using (StreamReader sR = new StreamReader(path + @"\input.txt"))
            {
                int j = 0;
                while (!sR.EndOfStream)
                {
                    int i = 0;
                    string temp = string.Empty;
                    file_string = sR.ReadLine();
                    file_string += '\0';
                    if (file_string[0] != '#')
                    {
                        while (file_string[i] != '\0')
                        {
                            while (file_string[i] != ' ')
                            {
                                if (file_string[i] == '\0')
                                    break;
                                temp += file_string[i];
                                i++;
                            }
                            vects[j] = Convert.ToDouble(temp);
                            temp = string.Empty;
                            j++;
                            if (file_string[i] != '\0')
                                i++;
                        }
                    }
                    else
                    { }
                }
            }
            using(StreamWriter sW = new StreamWriter(path + @"\output.txt"))
            {
                sW.Write(Convert.ToString(vects[0]*vects[3]+vects[1]*vects[4]+vects[2]*vects[5]) + " ");
                if (!(((vects[0] == 0) && (vects[1] == 0) && (vects[2] == 0)) || ((vects[3] == 0) && (vects[4] == 0) && (vects[5] == 0))))
                    sW.Write(Convert.ToString(Math.Acos((vects[0] * vects[3] + vects[1] * vects[4] + vects[2] * vects[5]) / 
                        Math.Sqrt(vects[0] * vects[0] + vects[1] * vects[1] + vects[2] * vects[2]) / 
                        Math.Sqrt(vects[3] * vects[3] + vects[4] * vects[4] + vects[5] * vects[5]))));
                else
                    sW.Write(0);
            }
        }
    }
}
