/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext, useRef } from "react"
import { Box as RadixThemesBox, Button as RadixThemesButton, Flex as RadixThemesFlex, Grid as RadixThemesGrid, Heading as RadixThemesHeading, Link as RadixThemesLink, Separator as RadixThemesSeparator, Text as RadixThemesText } from "@radix-ui/themes"
import NextLink from "next/link"
import { EventLoopContext, StateContexts } from "$/utils/context"
import { Event, isTrue, refs } from "$/utils/state"
import { GitBranch as LucideGitBranch, Github as LucideGithub, Mail as LucideMail, MapPin as LucideMapPin, Phone as LucidePhone } from "lucide-react"
import NextHead from "next/head"
import { jsx } from "@emotion/react"



export function Link_775ff05d6b63bf4aeb94383d4f8d5bb7 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_6cfb961d7733da31add9be84a2e5faa9 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.portfolio___states____states.toggle_code_modal", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesLink,
{css:({ ["cursor"] : "pointer", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),href:"#",onClick:on_click_6cfb961d7733da31add9be84a2e5faa9},
jsx("img",{css:({ ["width"] : "20px", ["height"] : "20px" }),src:"/code.svg"},)
,)
  )
}

export function Button_f34f96fa8af1a396afa4f9105bbb3f85 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_6f23ce5c9b97135a5cb5068e902aab3b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.portfolio___states____states.toggle_modal", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{css:({ ["backgroundColor"] : "#94A2AF", ["color"] : "#FFFFFF", ["&:hover"] : ({ ["backgroundColor"] : "#E2E8F0", ["color"] : "#94A2AF" }), ["borderRadius"] : "md", ["paddingInlineStart"] : "16px", ["paddingInlineEnd"] : "16px", ["paddingTop"] : "8px", ["paddingBottom"] : "8px" }),onClick:on_click_6f23ce5c9b97135a5cb5068e902aab3b},
"Contact"
,)
  )
}

export function Fragment_6c5f014c59784d2847c899cc10dc7536 () {
  
  const reflex___state____state__portfolio___states____states = useContext(StateContexts.reflex___state____state__portfolio___states____states)





  
  return (
    jsx(
Fragment,
{},
(reflex___state____state__portfolio___states____states.show_modal ? (jsx(
Fragment,
{},
jsx(
RadixThemesBox,
{css:({ ["position"] : "fixed", ["top"] : "0", ["left"] : "0", ["width"] : "100vw", ["height"] : "100vh", ["backgroundColor"] : "rgba(0, 0, 0, 0.4)", ["display"] : "flex", ["justifyContent"] : "center", ["alignItems"] : "center", ["zIndex"] : "1000" })},
jsx(
RadixThemesBox,
{css:({ ["padding"] : "24px", ["backgroundColor"] : "white", ["borderRadius"] : "10px", ["boxShadow"] : "2xl", ["width"] : "320px", ["zIndex"] : "1001", ["border"] : "1px solid #e2e8f0" })},
jsx(
RadixThemesHeading,
{size:"6"},
"Contact Information"
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["paddingTop"] : "8px", ["paddingBottom"] : "8px" }),direction:"column",gap:"4"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},
jsx(LucideMail,{},)
,jsx(
RadixThemesText,
{as:"p"},
"matiasfalconaro@gmail.com"
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},
jsx(LucidePhone,{},)
,jsx(
RadixThemesText,
{as:"p"},
"+54 9 (011) 15-3271-1841"
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},
jsx(LucideMapPin,{},)
,jsx(
RadixThemesText,
{as:"p"},
"Banfield, Buenos Aires, AR"
,),),),jsx(
RadixThemesFlex,
{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["marginTop"] : "16px" })},
jsx(Button_ec90983a37b66d1674cf31677cd402a7,{},)
,),),),)) : (jsx(
Fragment,
{},
null
,))),)
  )
}

export function Button_9485106e8386d371a09b8d496a31af47 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_6cfb961d7733da31add9be84a2e5faa9 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.portfolio___states____states.toggle_code_modal", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{css:({ ["backgroundColor"] : "#94A2AF", ["color"] : "#FFFFFF" }),onClick:on_click_6cfb961d7733da31add9be84a2e5faa9},
"Close"
,)
  )
}

export function Fragment_34eb81861b422a229818e9b85d7e4536 () {
  
  const reflex___state____state__portfolio___states____states = useContext(StateContexts.reflex___state____state__portfolio___states____states)





  
  return (
    jsx(
Fragment,
{},
(reflex___state____state__portfolio___states____states.show_code_modal ? (jsx(
Fragment,
{},
jsx(
RadixThemesBox,
{css:({ ["position"] : "fixed", ["top"] : "0", ["left"] : "0", ["width"] : "100vw", ["height"] : "100vh", ["backgroundColor"] : "rgba(0, 0, 0, 0.4)", ["display"] : "flex", ["justifyContent"] : "center", ["alignItems"] : "center", ["zIndex"] : "1000" })},
jsx(
RadixThemesBox,
{css:({ ["padding"] : "24px", ["backgroundColor"] : "white", ["borderRadius"] : "10px", ["boxShadow"] : "2xl", ["width"] : "320px", ["zIndex"] : "1001", ["border"] : "1px solid #e2e8f0" })},
jsx(
RadixThemesHeading,
{size:"6"},
"Page Info"
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["paddingTop"] : "8px", ["paddingBottom"] : "8px" }),direction:"column",gap:"4"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},
jsx(LucideGitBranch,{},)
,jsx(
RadixThemesText,
{as:"p"},
"v1.0.0"
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},
jsx("img",{css:({ ["width"] : "1.25em", ["height"] : "1.25em" }),src:"/python.svg"},)
,jsx(
RadixThemesText,
{as:"p"},
"Python (Reflex)"
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},
jsx(LucideGithub,{},)
,jsx(
RadixThemesLink,
{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),target:(true ? "_blank" : "")},
jsx(
NextLink,
{href:"https://github.com/matiasfalconaro/json_portfolio",passHref:true},
"Source code"
,),),),),jsx(
RadixThemesFlex,
{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["marginTop"] : "16px" })},
jsx(Button_9485106e8386d371a09b8d496a31af47,{},)
,),),),)) : (jsx(
Fragment,
{},
null
,))),)
  )
}

export function Button_ec90983a37b66d1674cf31677cd402a7 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_6f23ce5c9b97135a5cb5068e902aab3b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.portfolio___states____states.toggle_modal", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{css:({ ["backgroundColor"] : "#94A2AF", ["color"] : "#FFFFFF" }),onClick:on_click_6f23ce5c9b97135a5cb5068e902aab3b},
"Close"
,)
  )
}

export default function Component() {
    
  const ref_work = useRef(null); refs["ref_work"] = ref_work;
  const ref_education = useRef(null); refs["ref_education"] = ref_education;
  const ref_certificates = useRef(null); refs["ref_certificates"] = ref_certificates;
  const ref_projects = useRef(null); refs["ref_projects"] = ref_projects;




  return (
    jsx(
Fragment,
{},
jsx(
RadixThemesFlex,
{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["padding"] : "6", ["width"] : "100%" })},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["maxWidth"] : "900px" }),direction:"column",gap:"6"},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",css:({ ["padding"] : "4", ["borderBottom"] : "1px solid #e2e8f0", ["position"] : "sticky", ["top"] : "0", ["zIndex"] : "10", ["backgroundColor"] : "white", ["width"] : "100%" }),direction:"row",gap:"3"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"6"},
jsx(
RadixThemesLink,
{asChild:true,css:({ ["color"] : "#94A2AF", ["fontWeight"] : "bold", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},
jsx(
NextLink,
{href:"/",passHref:true},
"Home"
,),),jsx(
RadixThemesLink,
{asChild:true,css:({ ["color"] : "#94A2AF", ["fontWeight"] : "bold", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},
jsx(
NextLink,
{href:"#work",passHref:true},
"Work"
,),),jsx(
RadixThemesLink,
{asChild:true,css:({ ["color"] : "#94A2AF", ["fontWeight"] : "bold", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},
jsx(
NextLink,
{href:"#education",passHref:true},
"Education"
,),),jsx(
RadixThemesLink,
{asChild:true,css:({ ["color"] : "#94A2AF", ["fontWeight"] : "bold", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},
jsx(
NextLink,
{href:"#projects",passHref:true},
"Projects"
,),),),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},)
,jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(Link_775ff05d6b63bf4aeb94383d4f8d5bb7,{},)
,jsx(
RadixThemesLink,
{css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),href:"#",target:(true ? "_blank" : "")},
jsx("img",{css:({ ["width"] : "20px", ["height"] : "20px" }),src:"/github.svg"},)
,),jsx(
RadixThemesLink,
{css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),href:"#",target:(true ? "_blank" : "")},
jsx("img",{css:({ ["width"] : "20px", ["height"] : "20px" }),src:"/linkedin.svg"},)
,),),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["padding"] : "4" }),direction:"column",gap:"4"},
jsx(
RadixThemesGrid,
{columns:"2",css:({ ["width"] : "100%", ["alignItems"] : "center" }),gap:"4"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"column",gap:"3"},
jsx(
RadixThemesHeading,
{size:"8"},
"Matias Falconaro"
,),jsx(
RadixThemesText,
{as:"p",css:({ ["fontWeight"] : "bold" })},
"Software Developer"
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(Button_f34f96fa8af1a396afa4f9105bbb3f85,{},)
,jsx(
RadixThemesLink,
{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),download:true,target:(true ? "_blank" : "")},
jsx(
NextLink,
{href:"/resume.pdf",passHref:true},
jsx(
RadixThemesButton,
{css:({ ["backgroundColor"] : "#94A2AF", ["color"] : "#FFFFFF", ["&:hover"] : ({ ["backgroundColor"] : "#E2E8F0", ["color"] : "#94A2AF" }), ["borderRadius"] : "md", ["paddingInlineStart"] : "16px", ["paddingInlineEnd"] : "16px", ["paddingTop"] : "8px", ["paddingBottom"] : "8px" })},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(
RadixThemesText,
{as:"p"},
"Resume"
,),),),),),),),jsx(
RadixThemesBox,
{css:({ ["display"] : "flex", ["justifyContent"] : "flex-end" })},
jsx("img",{css:({ ["width"] : "150px", ["borderRadius"] : "5px" }),src:"/1736345293938.jfif"},)
,),),jsx(
RadixThemesText,
{as:"p",css:({ ["maxWidth"] : "800px", ["textAlign"] : "start" })},
"As a dedicated software developer, I am driven by the excitement of understanding and defining business requirements to create meaningful and impactful solutions. Analyzing processes, identifying needs, and developing strategies that not only solve business problems but also bring value and efficiency is at the core of my work. Some of my soft skills are being analytical, adaptable, collaborative, and committed. I also enjoy spending time with my family and friends, cycling, and swimming."
,),),jsx(RadixThemesSeparator,{size:"4"},)
,jsx(
RadixThemesHeading,
{id:"work",ref:ref_work,size:"6"},
"Work Experience"
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["maxWidth"] : "800px" }),direction:"column",gap:"4"},
jsx(
RadixThemesBox,
{css:({ ["marginBottom"] : "6" })},
jsx(
RadixThemesHeading,
{size:"5"},
"Python Developer @ Scienza Argentina"
,),jsx(
RadixThemesText,
{as:"p"},
"08/2024 \u2013 Present"
,),jsx(RadixThemesBox,{css:({ ["height"] : "1em" })},)
,jsx(
RadixThemesText,
{as:"p"},
"Led automation initiatives using Python and virtualization tools. Integrated OpenAI API for document auditing, prescription analysis, and cross-referencing with lab delivery notes. Developed and consumed APIs using FastAPI. Created comprehensive documentation and training resources. Championed DevOps practices with Git/GitHub and enforced clean architecture through OOP, SOLID principles, and modular design."
,),jsx(
"ul",
{css:({ ["direction"] : "column", ["listStyleType"] : "disc", ["marginLeft"] : "1.5rem" })},
jsx(
"li",
{},
"Process automation, AI, Systems migration"
,),),),jsx(
RadixThemesBox,
{css:({ ["marginBottom"] : "6" })},
jsx(
RadixThemesHeading,
{size:"5"},
"Python Developer @ Baitcon SA"
,),jsx(
RadixThemesText,
{as:"p"},
"12/2022 \u2013 08/2024"
,),jsx(RadixThemesBox,{css:({ ["height"] : "1em" })},)
,jsx(
RadixThemesText,
{as:"p"},
"Designed database schemas using ER diagrams, DDL, and SQL for efficient data storage and retrieval, and developed ETL processes to centralize data from various sources. Built RESTful APIs, integrated AI APIs and MMLs, ensured data security, and collaborated with data analysts, while managing data pipelines, backup strategies, and CI/CD pipelines for backend services."
,),jsx(
"ul",
{css:({ ["direction"] : "column", ["listStyleType"] : "disc", ["marginLeft"] : "1.5rem" })},
jsx(
"li",
{},
"Corporate software, automation and pipelining factory"
,),),),jsx(
RadixThemesBox,
{css:({ ["marginBottom"] : "6" })},
jsx(
RadixThemesHeading,
{size:"5"},
"FS Developer @ Freelance web developer"
,),jsx(
RadixThemesText,
{as:"p"},
"12/2018 \u2013 12/2023"
,),jsx(RadixThemesBox,{css:({ ["height"] : "1em" })},)
,jsx(
RadixThemesText,
{as:"p"},
"Developed and maintained web pages, including landing pages and e-commerce sites, focusing on enterprise clients. Leveraged Python for backend development and the Flask framework for web application interfaces."
,),jsx(
"ul",
{css:({ ["direction"] : "column", ["listStyleType"] : "disc", ["marginLeft"] : "1.5rem" })},
jsx(
"li",
{},
"Commercial landing pages development, deployment, hosting, maintenance and improvement"
,),),),jsx(
RadixThemesBox,
{css:({ ["marginBottom"] : "6" })},
jsx(
RadixThemesHeading,
{size:"5"},
"IT Support @ Pilcomayo SRL"
,),jsx(
RadixThemesText,
{as:"p"},
"01/2015 \u2013 02/2022"
,),jsx(RadixThemesBox,{css:({ ["height"] : "1em" })},)
,jsx(
RadixThemesText,
{as:"p"},
"Managed and maintained the company's IT infrastructure, including servers, networks, and workstations, ensuring performance, uptime, and secure connectivity through the configuration of routers, switches, firewalls, and VPNs. Provided technical support to employees, handled software installations and updates, managed user accounts and data backup solutions, enforced IT security policies, and coordinated with vendors for hardware and software procurement."
,),jsx(
"ul",
{css:({ ["direction"] : "column", ["listStyleType"] : "disc", ["marginLeft"] : "1.5rem" })},
jsx(
"li",
{},
"Systems maintenance, update and implementation"
,),),),jsx(
RadixThemesBox,
{css:({ ["marginBottom"] : "6" })},
jsx(
RadixThemesHeading,
{size:"5"},
"SAP Base Line Support @ Etex Group Argentina"
,),jsx(
RadixThemesText,
{as:"p"},
"11/2013 \u2013 12/2024"
,),jsx(RadixThemesBox,{css:({ ["height"] : "1em" })},)
,jsx(
RadixThemesText,
{as:"p"},
"Configured technical locations and maintenance plans in SAP to support asset management, ensuring efficient scheduling and execution of preventive maintenance tasks. Managed work orders, purchase requests, and equipment master data, while providing user training and support on SAP maintenance functionalities."
,),jsx(
"ul",
{css:({ ["direction"] : "column", ["listStyleType"] : "disc", ["marginLeft"] : "1.5rem" })},
jsx(
"li",
{},
"Started the SAP PM module implementation."
,),),),),jsx(RadixThemesSeparator,{size:"4"},)
,jsx(
RadixThemesHeading,
{id:"education",ref:ref_education,size:"6"},
"Education"
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["maxWidth"] : "800px" }),direction:"column",gap:"4"},
jsx(
RadixThemesBox,
{css:({ ["marginBottom"] : "6" })},
jsx(
RadixThemesHeading,
{size:"5"},
"Associate of Science Degree in Systems Analysis"
,),jsx(
RadixThemesText,
{as:"p"},
"UTN - Universidad Tecnologica Nacional"
,),jsx(
RadixThemesText,
{as:"p"},
"03/2023 \u2013 12/2026"
,),null
,null
,),jsx(
RadixThemesBox,
{css:({ ["marginBottom"] : "6" })},
jsx(
RadixThemesHeading,
{size:"5"},
"Diploma in Python development"
,),jsx(
RadixThemesText,
{as:"p"},
"UTN - Universidad Tecnologica Nacional"
,),jsx(
RadixThemesText,
{as:"p"},
"10/2023 \u2013 06/2024"
,),jsx(
RadixThemesText,
{as:"p"},
"GPA: 100.00"
,),null
,),),jsx(RadixThemesSeparator,{size:"4"},)
,jsx(
RadixThemesHeading,
{id:"certificates",ref:ref_certificates,size:"6"},
"Certificates"
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["maxWidth"] : "800px" }),direction:"column",gap:"4"},
jsx(
RadixThemesBox,
{css:({ ["marginBottom"] : "4" })},
jsx(
RadixThemesHeading,
{size:"5"},
"AWS Certified Solutions Architect"
,),jsx(
RadixThemesText,
{as:"p"},
"Issued by Amazon Web Servises on 06/2023"
,),null
,),jsx(
RadixThemesBox,
{css:({ ["marginBottom"] : "4" })},
jsx(
RadixThemesHeading,
{size:"5"},
"Google IT SUpport"
,),jsx(
RadixThemesText,
{as:"p"},
"Issued by Google on 03/2024"
,),null
,),),jsx(RadixThemesSeparator,{size:"4"},)
,jsx(
RadixThemesHeading,
{id:"projects",ref:ref_projects,size:"6"},
"Projects"
,),jsx(
RadixThemesBox,
{},
jsx(
RadixThemesGrid,
{columns:"3",gap:"4"},
jsx(
RadixThemesBox,
{css:({ ["padding"] : "16px", ["border"] : "1px solid #e2e8f0", ["borderRadius"] : "10px", ["boxShadow"] : "sm", ["backgroundColor"] : "white", ["width"] : "100%" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"column",gap:"3"},
jsx(
RadixThemesHeading,
{size:"5"},
"Expense manager"
,),jsx(
RadixThemesText,
{as:"p"},
"Desktop CRUD application for managing, tracking, exporting, and visually analyzing financial transactions including expenses and revenues."
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"2",wrap:"wrap"},
jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Python"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Data"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Desktop"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"SQLite3"
,),),jsx(
RadixThemesText,
{as:"p",css:({ ["fontWeight"] : "bold" })},
"Lead"
,),jsx(
RadixThemesLink,
{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),target:(true ? "_blank" : "")},
jsx(
NextLink,
{href:"https://github.com/matiasfalconaro/Tkinter_expense_manager",passHref:true},
"GitHub"
,),),),),jsx(
RadixThemesBox,
{css:({ ["padding"] : "16px", ["border"] : "1px solid #e2e8f0", ["borderRadius"] : "10px", ["boxShadow"] : "sm", ["backgroundColor"] : "white", ["width"] : "100%" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"column",gap:"3"},
jsx(
RadixThemesHeading,
{size:"5"},
"Investment App"
,),jsx(
RadixThemesText,
{as:"p"},
"Cloud-based application for mass data import, processing, and management of engineering project investment data, integrated for use with SAP Analytics Cloud."
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"2",wrap:"wrap"},
jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"SAP HANA"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"SAP BTP"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Python"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Flask"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Cloud"
,),),jsx(
RadixThemesText,
{as:"p",css:({ ["fontWeight"] : "bold" })},
"Lead"
,),null
,),),jsx(
RadixThemesBox,
{css:({ ["padding"] : "16px", ["border"] : "1px solid #e2e8f0", ["borderRadius"] : "10px", ["boxShadow"] : "sm", ["backgroundColor"] : "white", ["width"] : "100%" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"column",gap:"3"},
jsx(
RadixThemesHeading,
{size:"5"},
"GIS ETL pipeline"
,),jsx(
RadixThemesText,
{as:"p"},
"Back-end system to retrieve data from a database and GEOJSON files, process it, and compile into JSON files for geographic project information."
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"2",wrap:"wrap"},
jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"API"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"SAP HANA"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Python"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"GIS"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"GEOJSON"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Pandas"
,),),jsx(
RadixThemesText,
{as:"p",css:({ ["fontWeight"] : "bold" })},
"Associate"
,),null
,),),jsx(
RadixThemesBox,
{css:({ ["padding"] : "16px", ["border"] : "1px solid #e2e8f0", ["borderRadius"] : "10px", ["boxShadow"] : "sm", ["backgroundColor"] : "white", ["width"] : "100%" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"column",gap:"3"},
jsx(
RadixThemesHeading,
{size:"5"},
"Direction mgmt. App"
,),jsx(
RadixThemesText,
{as:"p"},
"Cloud platform for managing the import, export, and monitoring of engineering projects within a corporate enterprise's presidency."
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"2",wrap:"wrap"},
jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"API"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"SAP HANA"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Flask"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"SQLAlchemy"
,),),jsx(
RadixThemesText,
{as:"p",css:({ ["fontWeight"] : "bold" })},
"Associate"
,),null
,),),jsx(
RadixThemesBox,
{css:({ ["padding"] : "16px", ["border"] : "1px solid #e2e8f0", ["borderRadius"] : "10px", ["boxShadow"] : "sm", ["backgroundColor"] : "white", ["width"] : "100%" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"column",gap:"3"},
jsx(
RadixThemesHeading,
{size:"5"},
"DBs ETL Pipeline"
,),jsx(
RadixThemesText,
{as:"p"},
"Executable ETL pipeline for extracting, processing, validating, and transferring data from an Oracle DB to a HANA Cloud DB."
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"2",wrap:"wrap"},
jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"SAP HANA"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"SQLAlchemy"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"SQL Server"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"Automation"
,),),jsx(
RadixThemesText,
{as:"p",css:({ ["fontWeight"] : "bold" })},
"Associate"
,),null
,),),jsx(
RadixThemesBox,
{css:({ ["padding"] : "16px", ["border"] : "1px solid #e2e8f0", ["borderRadius"] : "10px", ["boxShadow"] : "sm", ["backgroundColor"] : "white", ["width"] : "100%" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"column",gap:"3"},
jsx(
RadixThemesHeading,
{size:"5"},
"Chat AWS"
,),jsx(
RadixThemesText,
{as:"p"},
"Cloud Python application leveraging OpenAI's API models for natural language queries to fetch data from a database."
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"2",wrap:"wrap"},
jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"API"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"AWS"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"PostgreSQL"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"OpenAI"
,),jsx(
RadixThemesBox,
{css:({ ["padding"] : "5px", ["borderRadius"] : "5px", ["color"] : "#2D3748", ["backgroundColor"] : "#EDF2F7", ["fontSize"] : "sm", ["fontWeight"] : "medium", ["margin"] : "1", ["display"] : "inline-block" })},
"ChatGpt"
,),),jsx(
RadixThemesText,
{as:"p",css:({ ["fontWeight"] : "bold" })},
"Lead"
,),null
,),),),),jsx(RadixThemesSeparator,{size:"4"},)
,jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",css:({ ["padding"] : "4", ["borderTop"] : "1px solid #e2e8f0", ["width"] : "100%", ["backgroundColor"] : "#f7fafc" }),direction:"column",gap:"2"},
jsx(
RadixThemesText,
{as:"p",css:({ ["fontSize"] : "sm" })},
"\u00a9 2025 Matias Falconaro."
,),),jsx(Fragment_6c5f014c59784d2847c899cc10dc7536,{},)
,jsx(Fragment_34eb81861b422a229818e9b85d7e4536,{},)
,),),jsx(
NextHead,
{},
jsx(
"title",
{},
"Matias Falconaro | Portfolio"
,),jsx("meta",{content:"favicon.ico",property:"og:image"},)
,),)
  )
}
