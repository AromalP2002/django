import { useState } from "react"

function TaskList(){
  const [data,setData]=useState([])
  return(
    <>
        <table>
            <thead>
                <tr>
                    <th>Task</th>
                    <th>Dis</th>

               </tr>

          </thead>
          <tbody>
              { data.mao((value,index)=>(
                <tr key={index}>
                  <td>{value.title}</td>
                  <td>{value.dis}</td>

                  

                </tr>
              ))}
          </tbody>

      </table>

  </>
  )
}
export default App
