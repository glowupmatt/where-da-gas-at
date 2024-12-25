import { useContext } from "react";
import { GoogleMapContext } from "../../context/GoogleMapContext";
import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  const { openSideMenu } = useContext(GoogleMapContext);

  if (!openSideMenu) { 
    return (
      <ul className="nav-data-container">
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
  
        <li>
          <ProfileButton />
        </li>
      </ul>
    );
  }
}

export default Navigation;
