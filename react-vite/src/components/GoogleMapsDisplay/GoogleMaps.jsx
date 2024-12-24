import { APIProvider } from "@vis.gl/react-google-maps";
import { useContext } from "react";
import { useGetCurrentLocation } from "../../hooks/useGetCurrentLocationHook";
import { useGetNearByStations } from "../../hooks/useGetNearByStations";
import SideMenuDisplay from "../SideMenu/SideMenuDisplay";
import "./GoogleMapsStyles.css";
import MapComponent from "./MapComponent";
import ControlButtonComponent from "./ControlButtonComponent";
import { GoogleMapContext } from "../../context/GoogleMapContext";

const API_KEY = import.meta.env.VITE_REACT_APP_GOOGLE_MAPS_API_KEY;

function GoogleMaps() {
  const center = useGetCurrentLocation();
  const nearbyStations = useGetNearByStations({
    center
  });

  //Here we are grabbing the values from the global state that influences the google maps display. All the values are coming from the GoogleMapContext.

  const { setNewCenter, openSideMenu, setOpenSideMenu } = useContext(GoogleMapContext);

  const handleButtonClick = () => {
    setNewCenter(center);

  };

  //This is the main component that will be rendered in the App.js
  //Here mostly all the the main components are being used
  //The side menu button and find current location button
  //As well as the map and the markers
  //If you need to find a component on the map you'll find it here

  return (
    <APIProvider apiKey={API_KEY}>
      {/* This is the button that will open the side menu when clicked. 
      If you want to edit it ctrl click into it.*/}
      <SideMenuDisplay nearbyStations={nearbyStations} openSideMenu={openSideMenu} />
      <ControlButtonComponent openSideMenu={openSideMenu} setOpenSideMenu={setOpenSideMenu} handleButtonClick={ handleButtonClick} />
      {/* Here we conditionally render the map component when the center has a value. 
      The center is coming from the useGetCurrentLocation hook. */}
      {center ? (
        <MapComponent />
      ) : (
        'Loading...'
      )}
    </APIProvider>
  );
}

export default GoogleMaps;
