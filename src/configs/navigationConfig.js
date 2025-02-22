import React from "react"
import * as Icon from "react-feather"
const navigationConfig = [
  {
    id: "dashboard",
    title: "Dashboard",
    type: "item",
    icon: <Icon.User size={20} />,
    navLink: "/dashboard"
  },
  {
    id: "portfolio",
    title: "Portfolios",
    type: "item",
    icon: <Icon.Coffee size={20} />,
    navLink: "/portfolios"
  },
]


export default navigationConfig
