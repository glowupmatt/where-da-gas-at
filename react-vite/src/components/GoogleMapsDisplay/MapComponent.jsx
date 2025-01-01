import { Map, AdvancedMarker } from "@vis.gl/react-google-maps";
import { useEffect, useContext } from "react";
import { GoogleMapContext } from "../../context/GoogleMapContext";
import "./MapComponent.css";
import GoogleMapsNearByLocations from "./GoogleMapsNearByLocations";
import InfoWindowComponent from "./InfoWindowComponent";

function MapComponent() {
  const {
    center,
    newCenter,
    setNewCenter,
    nearbyStations,
    selectedStation,
    map,
    zoom,
    setSelectedStation,
    setZoom,
  } = useContext(GoogleMapContext);

  //This useEffect will run when the map and newCenter is available
  useEffect(() => {
    if (map && newCenter) {
      map.setCenter(newCenter);
    }
  }, [map, newCenter, center]);

  const handleDragEnd = () => {
    if (map) {
      const newCenter = map.getCenter();
      setNewCenter({ lat: newCenter.lat(), lng: newCenter.lng() });
    }
  };
  return (
    //This is the main map rendered on the screen. There are a lot of prebuilt props that can be used to customize the map.
    <Map
      // onLoad={onLoad}
      onDragend={handleDragEnd}
      style={{ width: "100%", height: "100vh" }}
      defaultCenter={center}
      mapId={import.meta.env.VITE_REACT_APP_GOOGLE_MAP_ID || "e2ea39204ffcffc4"}
      defaultZoom={15}
      zoom={zoom}
      onZoomChanged={() => setZoom(map.getZoom())}
      onClick={() => selectedStation && setSelectedStation(null)}
      disableDefaultUI={true}
      gestureHandling={"greedy"}
    >
      <AdvancedMarker position={center}>
        <div>
          <img className="user-marker" src="/user.svg" width={32} height={32} />
        </div>
      </AdvancedMarker>
      {/* Here we conditionally render the Info Window Component. If a user selects a station the it will appear */}
      {selectedStation && <InfoWindowComponent />}
      {/* This is the component that will render all the nearby station markers on the map */}
      <GoogleMapsNearByLocations nearbyStations={nearbyStations} />
    </Map>
  );
}

export default MapComponent;
