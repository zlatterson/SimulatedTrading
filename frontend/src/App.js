
import './App.css';
import Dashboard from './containers/Dashboard';
import UserContainer from './containers/UserContainer';
import NavBar from './containers/NavBar';

import 'bootstrap/dist/css/bootstrap.min.css';
import Banner from './containers/Banner';
import Skills from './containers/Skills';
import { Projects } from './containers/Projects';


function App() {

  return (
<div className="App">
  <NavBar/>
  <Banner/>
  <Skills/>
  {/* <Projects/> */}
  <Dashboard/>
  {/* <UserContainer/> */}
</div>
  );
}

export default App;
